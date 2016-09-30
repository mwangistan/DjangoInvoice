import uuid
from django.db import models

PAYMENT_STATUS = (
		('paid', 'paid'),
		('not paid', 'not paid')
	)

PAYMENT_METHOD = (
		('Cash', 'Cash'),
		('M-Pesa', 'M-Pesa'),
		('Airtel-Money', 'Airtel-Money'),
		('Credit-Card', 'Credit-Card')
	)

class Invoice(models.Model):
	'''
	Stores invoice details
	'''
	
	invoice_id = models.CharField(max_length=8, editable=False, default=uuid.uuid4().hex[:8])
	amount = models.IntegerField(default=5000)
	payment_status = models.CharField(max_length=8, choices=PAYMENT_STATUS)
	name = models.CharField(max_length=50)
	id_number = models.CharField(max_length=8)
	date_of_birth = models.DateField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.invoice_id)




class Payment(models.Model):
	'''
	Stores payment transaction details
	'''

	invoice_id = models.ForeignKey(Invoice)
	payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD)
	date_paid = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.invoice_id)

