# Generated by Django 5.1.7 on 2025-05-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rice_mill', '0009_rename_sells_customer_sellsinvoices_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='previous_due',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sellcustomers',
            name='previous_due',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
