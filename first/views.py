from django.shortcuts import render

from . import models

def index(request):
    mobile = models.Mobile.objects.all()

    args = {'mobile' : mobile}

    return render(request, 'first/index.html', args)
