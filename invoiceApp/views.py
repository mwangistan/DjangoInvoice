from django.shortcuts import render, redirect
from invoiceApp.forms import *
from invoiceApp.models import *

def index(request):
	#Render the index page
	return render(request, 'index.html')

def apply(request):
	#Render application form and accept inputs to generate invoice
	if request.method == 'POST':
		form = ApplicationForm(request.POST)

		if form.is_valid():
			invoice = Invoice(amount=5000, payment_status='not paid', name=form.cleaned_data['name'],
				id_number=form.cleaned_data['id_number'], date_of_birth=form.cleaned_data['date_of_birth'])

			invoice.save()
			request.session['invoice'] = invoice.invoice_id

			return redirect('/payment')

		return render(request, 'apply.html', {'form':form})



	else:
		form = ApplicationForm()
		return render(request, 'apply.html', {'form':form})

def payment(request):
	#Make payment for a particular invoice
	invoice = Invoice.objects.get(invoice_id=request.session['invoice'])
	if request.method == 'POST':
		form = PaymentRequestForm(request.POST)

		if form.is_valid():
			payment = Payment(invoice_id=invoice, payment_method=form.cleaned_data['payment_method'])
			payment.save()
			invoice.payment_status = 'paid'
			invoice.save()
			return render(request, 'success.html', {'payment':payment, 'invoice':invoice})

		return render(request, 'payment.html', {'form':form, 'invoice':invoice})


	else:
		form = PaymentRequestForm()
		return render(request, 'payment.html', {'form':form, 'invoice':invoice})
