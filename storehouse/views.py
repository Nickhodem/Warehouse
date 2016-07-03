from django.shortcuts import render, Http404, get_object_or_404, RequestContext, \
    render_to_response, HttpResponseRedirect, HttpResponse
from django.http import HttpResponseNotFound
from .models import Ware
from .forms import WareForm, ProviderForm, ProductForm, OrderProduct, OrderForm, UserForm, UserProfileForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime


def enter(request):
    wares = Ware.objects.all()
    ware_views = Ware.objects.order_by('views')[:5]

    visits = int(request.COOKIES.get('visits', '1'))

    context_dict = {'wares': wares, 'views': ware_views, 'visits': visits}
    reset_last_visit_time = False
    response = render(request, 'storehouse/enter.html', context_dict)

    if 'last_visit' in request.COOKIES:
        # Yes it does! Get the cookie's value.
        last_visit = request.COOKIES['last_visit']
        # Cast the value to a Python date/time object.
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).days > 0:
            visits += 1
            # ...and flag that the cookie last visit needs to be updated
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so flag that it should be set.
        reset_last_visit_time = True
        context_dict['visits'] = visits
        # Obtain our Response object early so we can add cookie information.
        response = render(request, 'storehouse/enter.html', context_dict)
    print visits
    if reset_last_visit_time:
        response.set_cookie('last_visit', datetime.now())
        response.set_cookie('visits', visits)

    return response


'''
def waredetails_id(request, product_id):
    try:
        detail = Ware.objects.get(id=product_id)
    except Ware.DoesNotExist:
        raise Http404('any product has id %s' % product_id)

    return render(request, 'storehouse/ware_detail.html', {'detail': detail})
'''


@login_required
def waredetails_id(request, product_id):
    detail = get_object_or_404(Ware, id=product_id)
    return render(request, 'storehouse/ware_detail.html', {'detail': detail})


@login_required
def waredetails_name(request, product_name):
    detail = Ware.objects.filter(name=product_name)
    if not detail:
        return HttpResponseNotFound('any product has id %s' % product_name)
    else:
        return render(request, 'storehouse/ware_detail.html', {'detail': detail})


@login_required
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
            return render(request, 'storehouse/notbangla.html', {})
    else:
        form = WareForm()
        return render(request, 'storehouse/new_item.html', {'form': form})


@login_required
def newprovider(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enter')
        else:
            return render(request, 'storehouse/notbangla.html', {})
    else:
        form = ProviderForm()
        return render(request, 'storehouse/new_provider.html', {'form': form})


@login_required
def newproduct(request):
    form = ProductForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enter')
        else:
            return render(request, 'storehouse/notbangla.html', {})
    else:
        form = ProductForm()
        return render(request, 'storehouse/new_product.html', {'form': form})


@login_required
def neworder(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('enter')
        else:
            return render(request, 'storehouse/notbangla.html', {})
    else:
        form = OrderForm()
        return render(request, 'storehouse/new_order.html', {'form': form})


def getorder(request):
    if request.method == 'POST':
        form = OrderProduct(request.POST)
        if form.is_valid():
            return redirect('enter')
        else:
            return render(request, 'storehouse/notbangla.html', {})
    else:
        form = OrderProduct()

    return render(request, 'storehouse/get_order.html', {'form': form})


@login_required
def like_views(request):

    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']
    print 'cat id: ', cat_id
    likes = 0
    if cat_id:
        cat = Ware.objects.get(id=int(cat_id))
        if cat:
            likes = cat.views + 1
            cat.views = likes
            cat.save()

    return HttpResponse(likes)


def check_name(request):
    print 'get request ', request.GET['newviewname']
    if request.GET.has_key('newviewname'):
        try:
            Ware.objects.get(name=request.GET['newviewname'])
        except:
            return HttpResponse('nazwa wolna')
        else:
            return HttpResponse('nazwa zajeta')
    return HttpResponse('')

'''
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

    return render_to_response('storehouse/register.html',
                              {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)


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
        return render(request, 'storehouse/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/storehouse/')
'''
