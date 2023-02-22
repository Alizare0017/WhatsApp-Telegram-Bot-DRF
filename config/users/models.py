from django.db import models
# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length=32,null=False)
    userID = models.CharField(max_length=30,null=False)
    email = models.EmailField(null=True)
    token = models.CharField(null=True,max_length=40)
    charge = models.IntegerField(null=True)
    sent = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    exp_date = models.DateTimeField(null=True)
    last_charge_date = models.DateTimeField(null=True)
    changed_date = models.DateTimeField(null=True)
    change_count = models.IntegerField(default=0)
