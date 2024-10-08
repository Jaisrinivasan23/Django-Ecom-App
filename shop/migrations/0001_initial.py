# Generated by Django 5.0.6 on 2024-08-14 14:12

import django.db.models.deletion
import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catageory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('desc', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('trending', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('pro_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getfilename)),
                ('desc', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('original_price', models.FloatField()),
                ('sell_P', models.FloatField()),
                ('trending', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Catageory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catageory')),
            ],
        ),
    ]
