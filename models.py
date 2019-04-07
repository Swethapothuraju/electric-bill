
from django.db import models

# Create your models here.
class Reg(models.Model):
    Firstname=models.CharField(max_length=30)
    Middlename=models.CharField(max_length=30)
    Lastname=models.CharField(max_length=30)
    Username=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Confirmpassword=models.CharField(max_length=10)
    Contactno=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)

'''class Location(models.Model):
    State=models.CharField(max_length=30)
    Mandal=models.CharField(max_length=30)
    Village=models.CharField(max_length=30) ''' 
    


class Payment(models.Model):
    ConsumerNo=models.CharField(max_length=30)
    Billdate=models.CharField(max_length=30)
    Amount=models.CharField(max_length=30)
    
    
