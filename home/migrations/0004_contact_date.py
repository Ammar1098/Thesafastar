# Generated by Django 5.0.1 on 2024-02-05 19:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_ads_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
