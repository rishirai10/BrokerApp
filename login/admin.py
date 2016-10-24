from django.contrib import admin
from .models import *
# Register your models here.

class login_userAdmin(admin.ModelAdmin):
	list_display=["name","mobile","city","firm_name"]

admin.site.register(login_user,login_userAdmin)



