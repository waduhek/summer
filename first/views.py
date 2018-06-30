from django.shortcuts import render,get_object_or_404
from cart.forms import CartAddProductForm
from . import models
from first.models import Mobile

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

def category(request):
    return render(request, 'first/product-category.html')

def product_detail(request , product_id):
    product = get_object_or_404(Mobile , pk = product_id)
    cart_product_form = CartAddProductForm()
    return render(request ,'first/mobile.html' , {'product' : product , 'cart_product_form' : cart_product_form})