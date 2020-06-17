from django.contrib import admin
from .models import Topping, MenuItem, ItemType, Price, Cart

admin.site.register(Topping)
admin.site.register(MenuItem)
admin.site.register(ItemType)
admin.site.register(Price)
admin.site.register(Cart)