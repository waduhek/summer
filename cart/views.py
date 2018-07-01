from django.shortcuts import render , redirect , get_object_or_404
from django.views.decorators.http import require_POST
from first.models import Mobile
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request , pk):
	cart = Cart(request)
	mobile = get_object_or_404(Mobile , pk = pk)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(mobile = mobile , quantity = cd['quantity'] , update_quantity = cd['update'])
	return redirect('cart:cart_detail')

def cart_remove(request , pk):
	cart = Cart(request)
	mobile = get_object_or_404(Mobile , pk = pk)
	cart.remove(mobile)
	return redirect('cart:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial = { 'quantity' : item['quantity'] , 'update' : True})
	context = {'cart' : cart}
	return render(request , 'cart/detail.html', context)


