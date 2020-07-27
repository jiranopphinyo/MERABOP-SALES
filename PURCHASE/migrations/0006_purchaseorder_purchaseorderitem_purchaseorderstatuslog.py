# Generated by Django 3.0.8 on 2020-07-21 09:45

import PURCHASE.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0011_auto_20200720_2052'),
        ('PURCHASE', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.CharField(default=PURCHASE.models.increment_purchase_order_id, editable=False, max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Purchase Order ID')),
                ('date', models.DateField(default=django.utils.timezone.localdate, verbose_name='Purchase Order Date')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=20, verbose_name='Sub Total')),
                ('vat', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=20, verbose_name='Value Added Tax')),
                ('net_total', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=20, verbose_name='Net Total')),
                ('baht_text', models.CharField(default='', editable=False, max_length=200, verbose_name='Baht Text')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='Remark')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.Supplier', verbose_name='Supplier')),
                ('supplier_billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.SupplierAddress', verbose_name='Supplier Billing Address')),
                ('supplier_contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.SupplierContactPerson', verbose_name='Supplier Contact Person')),
                ('supplier_payment_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.SupplierPaymentTerm', verbose_name='SupplierPaymentTerm')),
            ],
            options={
                'verbose_name_plural': 'PURCHASE ORDER | PURCHASE ORDER',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderStatusLog',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Purchase Order Status Log ID')),
                ('user', models.CharField(max_length=50, verbose_name='User')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='Remark')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.PurchaseOrder', verbose_name='Purchase Order')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.PurchaseOrderStatus', verbose_name='Sales Order Status')),
            ],
            options={
                'verbose_name_plural': 'PURCHASE ORDER | PURCHASE ORDER STATUS LOG',
                'ordering': ['-purchase_order__id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Purchase Order Item ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Unit Price')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=20, verbose_name='Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.Product', verbose_name='Product')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_order_items', to='PURCHASE.PurchaseOrder', verbose_name='Purchase Order')),
            ],
            options={
                'verbose_name_plural': 'PURCHASE ORDER | PURCHASE ORDER ITEM',
                'ordering': ['-purchase_order__id'],
            },
        ),
    ]
