# Generated by Django 3.0 on 2020-08-01 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20200402_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_short_description',
        ),
    ]
