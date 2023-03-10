# Generated by Django 4.1.5 on 2023-03-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre de Usuario'),
        ),
    ]
