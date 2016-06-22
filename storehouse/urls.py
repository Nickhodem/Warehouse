from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.enter, name='enter'),
    url(r'^newitem/$', views.newitem, name='new_item'),
    url(r'^newprovider/$', views.newprovider, name='new_provider'),
    url(r'^newproduct/$', views.newproduct, name='new_product'),
    url(r'^getorder/$', views.getorder, name='get_order'),
    url(r'^neworder/$', views.neworder, name='new_order'),
    url(r'^ware/(?P<product_id>[0-9]+)/$', views.waredetails_id, name='detail_id'),
    url(r'^ware/(?P<product_name>\w+)/$', views.waredetails_name, name='detail_name'),
    url(r'^register/$', views.register, name='register'),
]