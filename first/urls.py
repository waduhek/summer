from django.urls import re_path
from django.views.generic import ListView, DetailView
from django.conf.urls import include

from . import views
from . import models


urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^about-us/$', views.about, name = 'about-us'),
    re_path(r'^product/laptops/$', ListView.as_view(queryset = models.Laptop.objects.all(), template_name = "first/laptop-card.html")),
    re_path(r'^product/laptops/(?P<pk>\d+)/$', DetailView.as_view(model = models.Laptop, template_name = "first/laptop.html")),
    re_path(r'^login/$', views.login, name = 'login'),
]
