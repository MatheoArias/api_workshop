# Generated by Django 4.1.5 on 2023-03-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employees_telephone_cel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='salarys_value',
        ),
        migrations.AlterField(
            model_name='employees',
            name='address_residence',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='telephone_cel',
            field=models.IntegerField(null=True, verbose_name='Número de celular'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='telephone_number',
            field=models.IntegerField(null=True, verbose_name='Número de teléfono'),
        ),
    ]
