from django.urls import re_path
from django.views.generic import ListView, DetailView

from . import views
from . import models


urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^about-us/$', views.about, name = 'about-us'),
    re_path(r'^shop/laptops/$', ListView.as_view(queryset = models.Laptop.objects.all(), template_name = "first/laptop-card.html")),
    re_path(r'^shop/laptops/(?P<pk>\d+)/$', DetailView.as_view(model = models.Laptop, template_name = "first/laptop.html")),
    re_path(r'^shop/mobiles/$', ListView.as_view(queryset = models.Mobile.objects.all(), template_name = "first/mobile-card.html")),
    re_path(r'^shop/mobiles/(?P<pk>\d+)/$', DetailView.as_view(model = models.Mobile, template_name = "first/mobile.html")),
]
