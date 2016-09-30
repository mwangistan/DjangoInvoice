from django import forms
from django.forms import ModelForm
from django.forms import extras
from invoiceApp.models import Payment

class ApplicationForm(forms.Form):
	'''
	Application form that generates an invoice
	'''
 	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
 															'placeholder': 'Your names'}))
 	id_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',
                                                                   'placeholder':'ID NO'}))
 	date_of_birth = forms.DateField(widget=extras.SelectDateWidget(years=range(1950, 2016)))

 	def clean_id_number(self):
 		#Check if id number is 8 digits
 		if len(str(self.cleaned_data['id_number'])) != 8:
 			raise forms.ValidationError("Incorrect ID number")

 		return self.cleaned_data['id_number']



class PaymentRequestForm(forms.ModelForm):
	'''
	Accepts payment and records payment transactions
	'''


	class Meta:
		model = Payment
		exclude = ['date_paid', 'invoice_id']
	