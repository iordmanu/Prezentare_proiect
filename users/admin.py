from __future__ import  unicode_literals
from django.contrib import admin
from users.models import MyUser

# Register your models here.
admin.site.register(MyUser)