# Generated by Django 4.0.5 on 2022-07-06 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='porduct',
            new_name='product',
        ),
    ]