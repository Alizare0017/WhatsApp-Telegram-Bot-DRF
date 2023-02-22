from django.contrib import admin
from .models import Factor

class FactorAdmin(admin.ModelAdmin):
    list_display = ['user', 'price']
admin.site.register(Factor, FactorAdmin)