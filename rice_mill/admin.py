from django.contrib import admin
from .models import Branch, CustomUser

# Register your models here.
admin.site.register(Branch)
admin.site.register(CustomUser)