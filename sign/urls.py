from django.urls import re_path

from . import views
from . import models

urlpatterns = [
	re_path(r'^$', views.login_view, name = 'login'),
    re_path(r'^signup/$', views.signup, name = 'signup'),
    re_path(r'^logout/$', views.logout_view, name = 'logout'),
]