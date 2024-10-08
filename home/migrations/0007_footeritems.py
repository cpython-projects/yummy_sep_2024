# Generated by Django 5.1.1 on 2024-10-05 17:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_reservation_is_processed'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=50)),
                ('item_description', ckeditor.fields.RichTextField()),
                ('item_icon', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
