# Generated by Django 3.2.9 on 2022-10-20 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]