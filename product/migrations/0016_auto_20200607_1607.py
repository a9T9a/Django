# Generated by Django 3.0.4 on 2020-06-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20200607_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]