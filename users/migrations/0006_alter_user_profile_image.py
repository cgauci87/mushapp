# Generated by Django 3.2.9 on 2022-10-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='static/images/user-default-avatar.png', upload_to='users/'),
        ),
    ]
