from django.contrib import admin

from .models import Customer,Order #import the  model we created 

# Register  the customer model

admin.site.register(Customer)

#Register the Order  model

admin.site.register(Order)
