from django.urls import re_path

from . import views
from . import models

urlpatterns = [
	re_path(r'^$', views.signup, name = 'signup'),
]