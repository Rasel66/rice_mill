# Generated by Django 5.1.7 on 2025-04-16 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rice_mill', '0003_remove_additemsdetails_items_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=250)),
                ('customer_name_bn', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chaul_qty', models.FloatField(blank=True, null=True)),
                ('khud_qty', models.FloatField(blank=True, null=True)),
                ('kura_qty', models.FloatField(blank=True, null=True)),
                ('chita_qty', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellsInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advance_amount', models.FloatField()),
                ('total_bill_amount', models.FloatField(blank=True, null=True)),
                ('paid_amount', models.FloatField()),
                ('balance', models.FloatField(blank=True, null=True)),
                ('prev_due', models.FloatField(blank=True, null=True)),
                ('current_due', models.FloatField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('chaul_qty', models.FloatField(blank=True, null=True)),
                ('chaul_unit_price', models.FloatField(blank=True, null=True)),
                ('chaul_total', models.FloatField(blank=True, null=True)),
                ('khud_qty', models.FloatField(blank=True, null=True)),
                ('khud_unit_price', models.FloatField(blank=True, null=True)),
                ('khud_total', models.FloatField(blank=True, null=True)),
                ('kura_qty', models.FloatField(blank=True, null=True)),
                ('kura_unit_price', models.FloatField(blank=True, null=True)),
                ('kura_total', models.FloatField(blank=True, null=True)),
                ('chita_qty', models.FloatField(blank=True, null=True)),
                ('chita_unit_price', models.FloatField(blank=True, null=True)),
                ('chita_total', models.FloatField(blank=True, null=True)),
                ('chaul_uom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chaul_invoices', to='rice_mill.uom')),
                ('chita_uom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chita_invoices', to='rice_mill.uom')),
                ('khud_uom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='khud_invoices', to='rice_mill.uom')),
                ('kura_uom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='kura_invoices', to='rice_mill.uom')),
                ('sells_customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rice_mill.sellcustomers')),
            ],
        ),
    ]
