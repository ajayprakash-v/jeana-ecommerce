# Generated by Django 4.2.1 on 2023-06-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeanaapp', '0003_variant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='about',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='baseprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
