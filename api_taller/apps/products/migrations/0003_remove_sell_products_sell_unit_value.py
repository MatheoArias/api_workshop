# Generated by Django 4.1.5 on 2023-02-04 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_buys_products_buys_unit_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell_products',
            name='sell_unit_value',
        ),
    ]