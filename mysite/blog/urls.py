from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^product/(?P<product_id>\d+)/$', views.click_product, name='click_product'),
    #url(r'^click_product/$', views.click_product, name= 'click_product'),
    url(r'^$', views.product_display, name = 'product_display'),
    url(r'^blog/add_product/$', views.add_product, name='add_product'),
    url(r'^blog/add_product/blog/save_product/$', views.save_product, name='save_product'),
]

