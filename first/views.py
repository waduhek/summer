from django.shortcuts import render

from . import models

def index(request):
    mobile = models.Mobile.objects.all()
    laptop = models.Laptop.objects.all()
    tablet = models.Tablet.objects.all()
    headset = models.Headset.objects.all()
    memorycard = models.MemoryCard.objects.all()
    powerbank = models.PowerBank.objects.all()
    charger = models.Charger.objects.all()


    args = {
        'mobile': mobile,
        'laptop': laptop,
        'tablet': tablet,
        'headset': headset,
        'memorycard': memorycard,
        'powerbank': powerbank,
        'charger': charger
    }

    return render(request, 'first/index.html', args)

def about(request):
    return render(request, 'first/about-us.html')

def product(request):
    return render(request, 'first/product-page.html')

def login(request):
    return render(request, 'first/login.html')
