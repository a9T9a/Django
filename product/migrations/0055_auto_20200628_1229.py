# Generated by Django 3.0.4 on 2020-06-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0054_auto_20200628_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]