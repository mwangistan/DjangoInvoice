from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoInvoice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'invoiceApp.views.index'),
    url(r'^apply/', 'invoiceApp.views.apply'),
    url(r'^payment/', 'invoiceApp.views.payment'),

]
