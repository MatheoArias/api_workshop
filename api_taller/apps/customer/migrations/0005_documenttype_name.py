# Generated by Django 4.1.5 on 2023-03-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_documenttype_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='documenttype',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Nombre'),
        ),
    ]