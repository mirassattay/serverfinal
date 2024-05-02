from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Almaty', 'Almaty'),
		('Nur-Sultan', 'Nur-Sultan'),
		('Shymkent', 'Shymkent'),
	)

	DISCRICT_CHOICES = (
		('Almaty', 'Almaty'), 
		('Nur-Sultan', 'Nur-Sultan'),
		('Shymkent', 'Shymkent'),
		('Taraz', 'Taraz'),
		('Aktau', 'Aktau'),
		('Taldykorgan', 'Taldykorgan'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Mastercard', 'Mastercard'),
		('Visa','Visa')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
