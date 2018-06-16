from django.contrib import admin
from .models import Mobile

class MobilesAdmin(admin.ModelAdmin):
	fields = ['manufacturer', 'model_name', 'display_size', 'cpu', 'ram', 'gpu']

admin.site.register(Mobile, MobilesAdmin)
