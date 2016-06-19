from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Ware
from .forms import WareForm, ProviderForm, ProductForm, OrderProduct,OrderForm
from django.utils import timezone
from django.shortcuts import redirect


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

