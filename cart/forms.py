from django import forms

class CartAddProductForm(forms.Form):

	quantity_choices = [(i, str(i)) for i in range(1, 11)]
	quantity = forms.TypedChoiceField(label = "Quantity ", choices = quantity_choices , coerce = int )
	update = forms.BooleanField(required = False , initial = False , widget = forms.HiddenInput)

