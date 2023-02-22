from django.contrib import admin
from users.models import User

class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'userID']
admin.site.register(User, UsersAdmin)