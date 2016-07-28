# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_saan_ka_woman', '0002_remove_orderinfo_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
