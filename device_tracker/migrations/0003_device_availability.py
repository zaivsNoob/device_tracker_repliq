# Generated by Django 4.2 on 2023-06-20 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_tracker', '0002_alter_devicelog_checkout_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
