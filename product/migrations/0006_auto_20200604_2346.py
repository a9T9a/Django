# Generated by Django 3.0.4 on 2020-06-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_images'),
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
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
