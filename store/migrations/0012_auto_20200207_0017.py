# Generated by Django 3.0 on 2020-02-07 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20200206_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='featured_products_specification',
            new_name='featured_products_description',
        ),
    ]
