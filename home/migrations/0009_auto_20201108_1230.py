# Generated by Django 3.1.3 on 2020-11-08 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='parent',
            new_name='category',
        ),
    ]