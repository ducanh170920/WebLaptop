# Generated by Django 3.1.3 on 2020-12-20 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('Checkout', '0007_auto_20201220_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_ship',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
