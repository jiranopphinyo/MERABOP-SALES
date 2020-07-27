# Generated by Django 3.0.8 on 2020-07-06 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0002_country'),
        ('PURCHASE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierAddress',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Supplier Address ID')),
                ('address_name', models.CharField(max_length=100, verbose_name='Address Name')),
                ('address_line_1', models.CharField(max_length=100, verbose_name='Address Line 1')),
                ('address_line_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address Line 2')),
                ('sub_district', models.CharField(max_length=100, verbose_name='Sub District')),
                ('district', models.CharField(max_length=100, verbose_name='District')),
                ('province', models.CharField(max_length=100, verbose_name='Province')),
                ('postal_code', models.CharField(max_length=10, verbose_name='ZIP/Postal Code')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Phone Number')),
                ('fax', models.CharField(blank=True, max_length=50, verbose_name='Fax Number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SETTINGS.Country', verbose_name='Country')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PURCHASE.Supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name_plural': 'SUPPLIER | SUPPLIER ADDRESS INFO',
                'ordering': ['supplier__id'],
            },
        ),
    ]
