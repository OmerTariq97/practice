# Generated by Django 5.1.1 on 2024-09-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_alter_todo_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
