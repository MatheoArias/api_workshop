# Generated by Django 4.1.5 on 2023-01-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Nombres y Apellidos')),
                ('documents_type', models.CharField(max_length=50, verbose_name='Tipo de documento')),
                ('documents_number', models.CharField(max_length=50, unique=True, verbose_name='Número de documento')),
                ('telephone_number', models.IntegerField(verbose_name='Número de telephone')),
                ('address_residence', models.CharField(max_length=200, verbose_name='Direccion')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
            ],
        ),
    ]
