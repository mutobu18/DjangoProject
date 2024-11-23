from django.db import models

# Create your models here.


#Stores the name and emails of customers and enforces uniqueness.

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)


    def  __str__(self):
        return self.name
    
class Order(models.Model):

        custsomer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orders')
        order_date=models.DateTimeField(auto_now_add=True)
        total_amount=models.DecimalField(max_digits=10,decimal_places=2)

        def __str__(self):
             return f"order {self.id} by {self.customer.name}"



