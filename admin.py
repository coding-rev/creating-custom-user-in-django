from django.contrib import admin
from .models import Users
# Register your models here.
class CustomUsers(admin.ModelAdmin):
	list_display = ['email','companies_name', 'country']
	list_filter  = ['country']
	random_fields= ['email', 'companies_name']

admin.site.register(Users, CustomUsers)


