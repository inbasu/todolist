# Generated by Django 4.1.5 on 2023-01-29 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_alter_task_created_alter_task_finished"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="created",
        ),
        migrations.RemoveField(
            model_name="task",
            name="finished",
        ),
    ]
