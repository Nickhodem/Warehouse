from django.shortcuts import render, Http404, get_object_or_404,RequestContext, \
    render_to_response, HttpResponseRedirect, HttpResponse
from django.http import HttpResponseNotFound
from .models import Ware
from .forms import WareForm, ProviderForm, ProductForm, OrderProduct, OrderForm, UserForm, UserProfileForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def enter(request):
    wares = Ware.objects.order_by('quantity')
    return render(request, 'storehouse/enter.html', {'wares': wares})

'''
def waredetails_id(request, product_id):
    try:
        detail = Ware.objects.get(id=product_id)
    except Ware.DoesNotExist:
        raise Http404('any product has id %s' % product_id)

    return render(request, 'storehouse/ware_detail.html', {'detail': detail})
'''


def waredetails_id(request, product_id):

    detail = get_object_or_404(Ware,id=product_id)
    return render(request, 'storehouse/ware_detail.html', {'detail': detail})


def waredetails_name(request, product_name):

    detail = Ware.objects.filter(name=product_name)

    if not detail:
        return HttpResponseNotFound('any product has id %s' % product_name)
    else:
        return render(request, 'storehouse/ware_detail.html', {'detail': detail})


def newitem(request):
    if request.method == "POST":
        form = WareForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_user = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('enter')
    else:
        form = WareForm()
        return render(request, 'storehouse/new_item.html', {'form': form})


def newprovider(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enter')
    else:
        form = ProviderForm()
        return render(request, 'storehouse/new_provider.html', {'form': form})


def newproduct(request):
    form = ProductForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enter')
    else:
        form = ProductForm()
        return render(request, 'storehouse/new_product.html', {'form': form})


def neworder(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enter')
    else:
        form = OrderForm()
        return render(request, 'storehouse/new_order.html', {'form': form})


def getorder(request):
    if request.method == 'POST':
        form = OrderProduct(request.POST)
        if form.is_valid():
            return redirect('enter')
    else:
        form = OrderProduct()

    return render(request, 'storehouse/get_order.html', {'form': form})


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('storehouse/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)


def user_login(request):

    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('Your account is disable')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('storehouse/login.html', {}, context)
