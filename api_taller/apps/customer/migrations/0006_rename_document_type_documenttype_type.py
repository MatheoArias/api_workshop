# Generated by Django 4.1.5 on 2023-03-13 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_documenttype_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documenttype',
            old_name='document_type',
            new_name='type',
        ),
    ]
