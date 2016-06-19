from django import forms
from .models import Ware, Provider, Product, Order


class WareForm(forms.ModelForm):

    class Meta:
        model = Ware
        fields = ('idx', 'name','quantity','provider_name','provider_url')


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = ('name', 'url', 'phone', 'email')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'model', 'wareparts', 'productparts')


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'product', 'client', 'notes')


class OrderProduct(forms.Form):

    availableproducts = forms.ModelMultipleChoiceField(queryset= Product.objects.all(), label='What we can serve?\n')
