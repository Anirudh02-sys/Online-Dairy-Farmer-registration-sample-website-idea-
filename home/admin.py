from django.contrib import admin
from .models import Company, Consumer, Farmer, Member
# Register your models here.

admin.site.register(Farmer)
admin.site.register(Consumer)
admin.site.register(Company)
