# Generated by Django 3.0.8 on 2020-07-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0009_auto_20200719_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReportContactMethod',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Daily Report Contact Method ID')),
                ('daily_report_contact_method', models.CharField(max_length=20, verbose_name='Daily Report Contact Method')),
            ],
            options={
                'verbose_name_plural': 'SETTINGS | DAILY REPORT | DAILY REPORT CONTACT METHOD',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DailyReportType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Daily Report Type ID')),
                ('daily_report_type', models.CharField(max_length=20, verbose_name='Daily Report Type')),
            ],
            options={
                'verbose_name_plural': 'SETTINGS | DAILY REPORT | DAILY REPORT TYPE',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderStatus',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Purchase Order Status ID')),
                ('purchase_order_status', models.CharField(max_length=20, verbose_name='Purchase Order Status')),
            ],
            options={
                'verbose_name_plural': 'SETTINGS | PURCHASE ORDER | PURCHASE ORDER STATUS',
                'ordering': ['id'],
            },
        ),
    ]
