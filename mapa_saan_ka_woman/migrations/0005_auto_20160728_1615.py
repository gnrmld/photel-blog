# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapa_saan_ka_woman', '0004_auto_20160728_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='client_id',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='mapa_saan_ka_woman.ClientInfo', null=True, related_name='order'),
        ),
    ]
