# Generated by Django 5.0.1 on 2024-02-05 19:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productcontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontact',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
