# Generated by Django 4.1.5 on 2023-04-04 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_discounts_sell_products_discounts_id'),
        ('bill', '0014_rename_customer_id_bill_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='discounts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.discounts', verbose_name='Descuento'),
        ),
        migrations.DeleteModel(
            name='Discounts',
        ),
    ]
