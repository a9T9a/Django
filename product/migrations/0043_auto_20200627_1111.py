# Generated by Django 3.0.4 on 2020-06-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0042_auto_20200627_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='modified_image',
            field=models.ImageField(blank=True, null=True, upload_to='modified_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
