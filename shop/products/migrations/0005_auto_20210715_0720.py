# Generated by Django 3.2.5 on 2021-07-15 07:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210712_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во на скаладе'),
        ),
    ]