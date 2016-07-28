from django.contrib import admin

from .models import DeliveryManInfo, DeliveryManStatus, OrderInfo, ItemInfo, ClientInfo
admin.site.register(DeliveryManInfo)
admin.site.register(DeliveryManStatus)
admin.site.register(OrderInfo)
admin.site.register(ItemInfo)
admin.site.register(ClientInfo)