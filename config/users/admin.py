from django.contrib import admin
from users.models import users

class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_id']
admin.site.register(users, UsersAdmin)