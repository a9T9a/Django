# Generated by Django 3.0.4 on 2020-06-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0046_auto_20200627_1203'),
    ]

    operations = [
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
    ]
