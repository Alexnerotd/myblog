from django.contrib import admin
from accounts.models import MyUser
from blog.models import Blog

# Register your models here.

admin.site.site_header = "API BLOGS"

admin.site.register(MyUser)
admin.site.register(Blog)