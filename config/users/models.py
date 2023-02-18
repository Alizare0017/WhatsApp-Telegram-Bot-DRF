from django.db import models

# Create your models here.

class users(models.Model):
    
    user_id = models.CharField(max_length=30,null=False)
    username = models.CharField(max_length=32,null=False)
    email = models.EmailField(null=True)
    token = models.CharField(max_length=50)
    plan = models.IntegerField(null=True)
    sent = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    exp_date = models.DateTimeField(null=True)
    change_count = models.IntegerField(default=3)
