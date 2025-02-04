# Generated by Django 5.1.5 on 2025-01-31 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_remove_city_personalised_price'),
        ('parcel', '0006_alter_parcel_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcel_city', to='city.city'),
        ),
    ]
