# Generated by Django 5.1.5 on 2025-01-24 16:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parcel', '0001_initial'),
        ('zone', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcel_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='parcel',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcel_zone', to='zone.zone'),
        ),
    ]