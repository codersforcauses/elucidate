# Generated by Django 4.0.6 on 2022-07-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quiz_create", "0002_remove_quiz_details_creator_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question_answer",
            name="answer_number",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="quiz_question",
            name="question_number",
            field=models.PositiveIntegerField(default=1),
        ),
    ]