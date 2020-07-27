# Generated by Django 3.0.8 on 2020-07-21 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SALES', '0009_auto_20200719_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyreport',
            options={'ordering': ['-date'], 'verbose_name_plural': 'DAILY REPORT | DAILY REPORT'},
        ),
        migrations.AlterModelOptions(
            name='dailyreportitem',
            options={'ordering': ['-daily_report__id'], 'verbose_name_plural': 'DAILY REPORT | DAILY REPORT ITEM'},
        ),
        migrations.AlterModelOptions(
            name='purchaserequisition',
            options={'ordering': ['-id'], 'verbose_name_plural': 'PURCHASE REQUISITION | PURCHASE REQUISITION'},
        ),
        migrations.AlterModelOptions(
            name='purchaserequisitionitem',
            options={'ordering': ['-purchase_requisition__id'], 'verbose_name_plural': 'PURCHASE REQUISITION | PURCHASE REQUISITION ITEM'},
        ),
        migrations.AlterModelOptions(
            name='purchaserequisitionstatuslog',
            options={'ordering': ['-purchase_requisition__id'], 'verbose_name_plural': 'PURCHASE REQUISITION | PURCHASE REQUISITION STATUS LOG'},
        ),
        migrations.AlterModelOptions(
            name='quotation',
            options={'ordering': ['-id'], 'verbose_name_plural': 'QUOTATION | QUOTATION'},
        ),
        migrations.AlterModelOptions(
            name='quotationitem',
            options={'ordering': ['-quotation__id'], 'verbose_name_plural': 'QUOTATION | QUOTATION ITEM'},
        ),
        migrations.AlterModelOptions(
            name='quotationstatuslog',
            options={'ordering': ['-quotation__id'], 'verbose_name_plural': 'QUOTATION | QUOTATION STATUS LOG'},
        ),
        migrations.AlterModelOptions(
            name='salesorder',
            options={'ordering': ['-id'], 'verbose_name_plural': 'SALES ORDER | SALES ORDER'},
        ),
        migrations.AlterModelOptions(
            name='salesorderitem',
            options={'ordering': ['-sales_order__id'], 'verbose_name_plural': 'SALES ORDER | SALES ORDER ITEM'},
        ),
        migrations.AlterModelOptions(
            name='salesorderstatuslog',
            options={'ordering': ['-sales_order__id'], 'verbose_name_plural': 'SALES ORDER | SALES ORDER STATUS LOG'},
        ),
    ]