# Generated by Django 3.0.4 on 2020-06-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_auto_20200612_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
