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
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^like_category/$', views.like_views, name='like_category'),
    url(r'^check_name/$', views.check_name, name = 'check_name')
]