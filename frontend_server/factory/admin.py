from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Password)
admin.site.register(Employee)
admin.site.register(Tag)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(CustomerOrder)
admin.site.register(Document)
admin.site.register(Task)