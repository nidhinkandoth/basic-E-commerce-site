from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^blog/product_display/$', views.product_display, name = 'product_display'),
    url(r'^blog/add_product/$', views.add_product, name='add_product'),
    url(r'^blog/save_product/$', views.save_product, name='save_product'),
]

