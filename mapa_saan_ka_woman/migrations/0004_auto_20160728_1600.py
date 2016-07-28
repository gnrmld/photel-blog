# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_saan_ka_woman', '0003_orderinfo_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='item_id',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='item',
            field=models.ForeignKey(to='mapa_saan_ka_woman.ItemInfo', blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='order', null=True),
        ),
    ]
