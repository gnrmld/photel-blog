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
'''
    access item/client
    order1 = OrderInfo.objects.get(pk=1)
    order1.item / order1.client
    then access its properties/methods by
    order1.item.name / order1.item.price
'''
    item = models.ForeignKey('ItemInfo',  related_name='order', blank=True, null=True, on_delete=models.PROTECT)
    client = models.ForeignKey('ClientInfo', related_name='order', blank=True, null=True, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    preferred_date = models.DateTimeField(blank=True, null=True)
    payment_method = models.CharField(max_length=10)
    drop_off_address = models.CharField(max_length=255)

    def __str__(self):
        return self.item.name


class ItemInfo(models.Model):
    '''
    access OrderInfo
    item1 = ItemInfo.objects.get(pk=1)
    item1.order.all() 
    item1.order.get(pk=3)
    item.order.filter()
    '''
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