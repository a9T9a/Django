# Generated by Django 3.0.4 on 2020-06-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20200611_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('false', 'Hayır')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('false', 'Hayır')], max_length=10),
        ),
    ]
