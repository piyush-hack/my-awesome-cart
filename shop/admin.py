from django.contrib import admin
from .models import Product, Contact
from .models import Chat
from .models import Orders, OrderUpdate

admin.site.register(Product)
admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)


