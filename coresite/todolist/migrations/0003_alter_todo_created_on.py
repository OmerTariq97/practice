# Generated by Django 5.1.1 on 2024-09-12 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todo_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 12, 18, 13, 28, 349068)),
        ),
    ]