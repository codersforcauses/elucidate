# Generated by Django 4.0.6 on 2022-07-13 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_create', '0005_remove_quiz_objective_quiz_details_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz_Tag',
            new_name='Question_Tag',
        ),
    ]
