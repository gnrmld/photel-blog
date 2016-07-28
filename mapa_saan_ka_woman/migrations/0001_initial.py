# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('sign_up_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_order_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryManInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryManStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('total_delivery_time', models.TimeField()),
                ('driver_id', models.ForeignKey(to='mapa_saan_ka_woman.DeliveryManInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('preferred_date', models.DateTimeField(null=True, blank=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_method', models.CharField(max_length=10)),
                ('drop_off_address', models.CharField(max_length=255)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mapa_saan_ka_woman.ClientInfo')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mapa_saan_ka_woman.ItemInfo')),
            ],
        ),
        migrations.AddField(
            model_name='deliverymanstatus',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mapa_saan_ka_woman.OrderInfo'),
        ),
    ]
