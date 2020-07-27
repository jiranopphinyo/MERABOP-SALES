# Generated by Django 3.0.8 on 2020-07-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SETTINGS', '0004_packingmaterial_packingtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='Company Name')),
                ('brand_name', models.CharField(max_length=50, verbose_name='Brand Name')),
            ],
            options={
                'verbose_name_plural': 'COMPANY | COMPANY SETTINGS',
                'ordering': ['company_name'],
            },
        ),
    ]