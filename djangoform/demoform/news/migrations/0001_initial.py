# Generated by Django 3.1.3 on 2020-11-03 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('time_create', models.DateTimeField(default=datetime.datetime(2020, 11, 3, 10, 35, 40, 840667))),
            ],
        ),
    ]
