# Generated by Django 4.1.5 on 2023-03-17 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0013_alter_bill_customer_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='discounts_id',
            new_name='discounts',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='employee_id',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='payment_medium_id',
            new_name='payment_medium',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='vehicle_id',
            new_name='vehicle',
        ),
    ]