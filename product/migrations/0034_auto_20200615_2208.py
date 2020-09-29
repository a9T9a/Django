# Generated by Django 3.0.4 on 2020-06-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_auto_20200615_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='category',
        ),
        migrations.AlterField(
            model_name='brand',
            name='status',
            field=models.CharField(choices=[('false', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('false', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]
