# Generated by Django 4.0.5 on 2022-07-06 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_rename_porduct_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
