from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomUsers

class UsersAdmin(admin.ModelAdmin):
    list_display = ['username','email','gender','phone']
    search_fields = ['username','email']
    readonly_fields = ['password']
    list_filter = ['gender']

admin.site.register(CustomUsers,UsersAdmin)