# Generated by Django 3.0.8 on 2020-07-23 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0012_livingarrangement_nationality_race'),
        ('PURCHASE', '0006_purchaseorder_purchaseorderitem_purchaseorderstatuslog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier_payment_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.SupplierPaymentTerm', verbose_name='Supplier Payment Term'),
        ),
        migrations.AlterField(
            model_name='purchaseorderstatuslog',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.PurchaseOrderStatus', verbose_name='Purchase Order Status'),
        ),
    ]
