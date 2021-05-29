from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Password)
admin.site.register(Employee)
admin.site.register(Tag)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
