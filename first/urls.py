from django.urls import re_path
from django.views.generic import ListView, DetailView

from . import views
from . import models


urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^about-us/$', views.about, name = 'about-us'),
    re_path(r'^shop/categories/laptops/$', ListView.as_view(queryset = models.Laptop.objects.all(), template_name = "first/laptop-card.html")),
    re_path(r'^shop/categories/laptops/(?P<pk>\d+)/$', DetailView.as_view(model = models.Laptop, template_name = "first/laptop.html")),
    re_path(r'^shop/categories/mobiles/$', ListView.as_view(queryset = models.Mobile.objects.all(), template_name = "first/mobile-card.html")),
    re_path(r'^shop/categories/mobiles/(?P<pk>\d+)/$', DetailView.as_view(model = models.Mobile, template_name = "first/mobile.html")),
    re_path(r'^shop/categories/tablets/$', ListView.as_view(queryset = models.Tablet.objects.all(), template_name = "first/tablet-card.html")),
    re_path(r'^shop/categories/tablets/(?P<pk>\d+)/$', DetailView.as_view(model = models.Tablet, template_name = "first/tablet.html")),
    re_path(r'^shop/categories/headsets/$', ListView.as_view(queryset = models.Headset.objects.all(), template_name = "first/headset-card.html")),
    re_path(r'^shop/categories/headsets/(?P<pk>\d+)/$', DetailView.as_view(model = models.Headset, template_name = "first/headset.html")),
    re_path(r'^shop/categories/powerbanks/$', ListView.as_view(queryset = models.PowerBank.objects.all(), template_name = "first/powerbank-card.html")),
    re_path(r'^shop/categories/powerbanks/(?P<pk>\d+)/$', DetailView.as_view(model = models.PowerBank, template_name = "first/powerbank.html")),
    re_path(r'^shop/categories/memorycards/$', ListView.as_view(queryset = models.MemoryCard.objects.all(), template_name = "first/memorycard-card.html")),
    re_path(r'^shop/categories/memorycards/(?P<pk>\d+)/$', DetailView.as_view(model = models.MemoryCard, template_name = "first/memorycard.html")),
    re_path(r'^shop/categories/chargers/$', ListView.as_view(queryset = models.Charger.objects.all(), template_name = "first/charger-card.html")),
    re_path(r'^shop/categories/chargers/(?P<pk>\d+)/$', DetailView.as_view(model = models.Charger, template_name = "first/charger.html")),
    re_path(r'^shop/categories/$', views.category, name = 'category')
]

