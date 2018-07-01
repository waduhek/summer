from decimal import Decimal
from django.conf import settings
from first.models import Mobile


class Cart(object):

	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, mobile , quantity = 1, update_quantity = False):
		mobile_id = str(mobile.id)
		if mobile_id not in self.cart:
			self.cart[mobile_id] = {'quantity' : 0 , 'price' : str(mobile.Price)}
		if update_quantity: 
			self.cart[mobile_id]['quantity'] = quantity
		else:
			self.cart[mobile_id]['quantity']  += quantity
		self.save()

	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

	def remove(self, mobile):
		mobile_id = str(mobile.id)
		if mobile_id in self.cart:
			del self.cart[mobile_id]
			self.save()

	def __iter__(self):
		mobile_ids = self.cart.keys()
		mobiles = Mobile.objects.filter(id__in = mobile_ids)
		for mobile in mobiles:
			self.cart[str(mobile.id)]['mobile'] = mobile
		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True





