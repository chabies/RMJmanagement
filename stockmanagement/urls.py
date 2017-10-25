from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'(?P<category_pk>\d+)/(?P<subcategory_pk>\d+)/$', views.product_profiles, name='product_profiles'),
    url(r'(?P<category_pk>\d+)/(?P<subcategory_pk>\d+)/add_product/$', views.add_product, name='add_product'),
    url(r'(?P<pk>\d+)/$', views.subcategory_list, name='subcategory_list'),
    url(r'^$', views.category_list, name='category_list'),

]
