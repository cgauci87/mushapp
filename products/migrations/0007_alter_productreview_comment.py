# Generated by Django 3.2.9 on 2022-10-28 01:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='comment',
            field=models.TextField(max_length=800, validators=[django.core.validators.MinLengthValidator(50, 'the field must contain at least 50 characters')]),
        ),
    ]
