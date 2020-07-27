# Generated by Django 3.0.8 on 2020-07-06 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0004_packingmaterial_packingtype'),
        ('PURCHASE', '0004_supplierpaymentterm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Product ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('net_weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Net Weight')),
                ('gross_weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Gross Weight')),
                ('weighing_unit', models.CharField(default='KG', max_length=20, verbose_name='Weighing Unit')),
                ('cbm', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Cubic Metre')),
                ('characteristic', models.TextField(blank=True)),
                ('total_remaining_amount', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=20, verbose_name='Total Remaining Amount')),
                ('suggested_sales_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Suggested Sales Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('manufactured_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufactured_country', to='SETTINGS.Country', verbose_name='Manufactured Country')),
                ('packing_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.PackingMaterial', verbose_name='Packing Material')),
                ('packing_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.PackingType', verbose_name='Packing Type')),
                ('shipped_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipped_country', to='SETTINGS.Country', verbose_name='Shipped Country')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.Supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name_plural': 'PRODUCT | PRODUCT GENERAL INFO',
                'ordering': ['id'],
            },
        ),
    ]
