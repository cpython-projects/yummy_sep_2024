# Generated by Django 5.1.1 on 2024-10-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_footeritems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footeritems',
            name='item_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
