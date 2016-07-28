from django.db import models
from django.utils import timezone

class DeliveryManInfo(models.Model):
    name = models.CharField(max_length=80)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class DeliveryManStatus(models.Model):
    driver_id = models.ForeignKey('DeliveryManInfo', on_delete=models.CASCADE)
    order_id = models.ForeignKey('OrderInfo', on_delete=models.PROTECT)
    total_delivery_time = models.TimeField(auto_now=False, auto_now_add=False)


class OrderInfo(models.Model):
    item_id = models.ForeignKey('ItemInfo', on_delete=models.PROTECT)
    client_id = models.ForeignKey('ClientInfo', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    preferred_date = models.DateTimeField(blank=True, null=True)
    payment_method = models.CharField(max_length=10)
    drop_off_address = models.CharField(max_length=255)



class ItemInfo(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class ClientInfo(models.Model):
    name = models.CharField(max_length=100)
    sign_up_date = models.DateTimeField(default=timezone.now)
    last_order_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name