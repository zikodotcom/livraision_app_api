# Generated by Django 5.1.5 on 2025-01-31 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0003_initial'),
        ('parcel', '0004_parcel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcel',
            name='zone',
        ),
        migrations.AddField(
            model_name='parcel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcel_zone', to='city.city'),
            preserve_default=False,
        ),
    ]
