# Generated by Django 4.1.5 on 2023-04-26 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_percentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sell_products',
            name='discount_value',
        ),
        migrations.AlterField(
            model_name='discounts',
            name='types',
            field=models.CharField(max_length=100, verbose_name='Tipo'),
        ),
    ]