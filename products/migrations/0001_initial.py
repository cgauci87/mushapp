# Generated by Django 3.2.9 on 2022-10-22 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('is_hide', models.BooleanField(default=False)),
                ('approval_status', models.CharField(blank=True, choices=[('1', 'Pending'), ('2', 'Approved'), ('3', 'Rejected')], default='1', max_length=25, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(default=0.0)),
                ('category', models.CharField(blank=True, max_length=150, null=True)),
                ('session', models.CharField(blank=True, max_length=150, null=True)),
                ('approval_status', models.CharField(blank=True, choices=[('0', 'Pending'), ('1', 'Approved'), ('2', 'Rejected')], default='0', max_length=25, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
