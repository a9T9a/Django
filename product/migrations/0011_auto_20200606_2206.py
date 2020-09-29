# Generated by Django 3.0.4 on 2020-06-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_brand_category'),
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
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('False', 'Hayır'), ('True', 'Evet')], max_length=10),
        ),
    ]