from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gender}"

    class Meta:
        db_table = 'customers'

class Deposit(models.Model):
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='deposits') # many to one
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.first_name} - {self.amount}"

    class Meta:
        db_table = 'deposits'


class Address(models.Model):
    street = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    sub_county = models.CharField(max_length=50)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='address') # one to one
    class Meta:
        db_table = 'addresses'

# run the migrations
# python manage.py makemigrations
# python manage.py migrate