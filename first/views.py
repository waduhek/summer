from django.shortcuts import render

from . import models

def index(request):
    mobile = models.Mobile.objects.all()
    laptop = models.Laptop.objects.all()

    args = {
        'mobile': mobile,
        'laptop': laptop
    }

    return render(request, 'first/index.html', args)
