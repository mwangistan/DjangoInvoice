from django.contrib import admin
from invoiceApp.models import *

class InvoiceAdmin(admin.ModelAdmin):
	pass

class PaymentAdmin(admin.ModelAdmin):
	pass

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)
