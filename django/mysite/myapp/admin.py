from django.contrib import admin
from .models import EMPLOYEE,STORES
class PostAdminSite(admin.AdminSite):
    site_header = "Bonjour Sales"
    site_title = "Bonjour Sales Admin Portal"
    index_title = "Welcome to Bonjour Sales"

post_admin_site = PostAdminSite(name='post_admin')
# Register your models here.
admin.site.register(EMPLOYEE)
post_admin_site.register(EMPLOYEE)
