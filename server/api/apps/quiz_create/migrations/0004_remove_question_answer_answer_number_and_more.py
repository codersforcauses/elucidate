# Generated by Django 4.0.6 on 2022-07-12 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_create', '0003_question_answer_answer_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_answer',
            name='answer_number',
        ),
        migrations.RemoveField(
            model_name='quiz_question',
            name='question_number',
        ),
    ]
