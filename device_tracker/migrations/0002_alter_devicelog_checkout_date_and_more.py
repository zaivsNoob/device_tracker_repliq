# Generated by Django 4.2 on 2023-06-20 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicelog',
            name='checkout_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicelog',
            name='return_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
