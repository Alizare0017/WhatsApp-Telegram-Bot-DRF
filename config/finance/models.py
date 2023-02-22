from django.db import models
from users.models import User

# Create your models here.

class Factor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charge = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now=True)