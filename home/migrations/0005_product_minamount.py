# Generated by Django 3.1.3 on 2020-11-08 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='minamount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
