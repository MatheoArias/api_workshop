# Generated by Django 4.1.5 on 2023-04-05 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_discounts_id_sell_products_discount_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_products',
            name='discount_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.discounts', verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='sell_products',
            name='discount_value',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True, verbose_name='Valor con descuento'),
        ),
    ]
