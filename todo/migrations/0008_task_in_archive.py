# Generated by Django 4.1.5 on 2023-02-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0007_remove_task_in_archive"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="in_archive",
            field=models.BooleanField(default=False),
        ),
    ]