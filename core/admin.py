from django.contrib import admin
from accounts.models import MyUser

# Register your models here.

admin.site.site_header = "API BLOGS"

admin.site.register(MyUser)