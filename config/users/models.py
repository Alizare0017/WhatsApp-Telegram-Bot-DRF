from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length=32,null=False)
    userID = models.CharField(max_length=30,null=False)
    email = models.EmailField(null=True,default=None)
    token = models.CharField(null=True,max_length=40,default=None)
    charge = models.IntegerField(null=True,default=0)
    sent = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    exp_date = models.DateTimeField(default=timezone.now)
    last_charge_date = models.DateTimeField(null=True,default=None)
    changed_date = models.DateTimeField(default=timezone.now)
    change_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.userID