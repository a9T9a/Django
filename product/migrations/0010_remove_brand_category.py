# Generated by Django 3.0.4 on 2020-06-06 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_brand_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
    ]
