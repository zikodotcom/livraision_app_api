# Generated by Django 5.1.5 on 2025-01-24 16:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDocument',
            fields=[
                ('id_invoice_doc', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
    ]