# Generated by Django 4.0.6 on 2022-11-22 08:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shared_models", "0004_rename_text_answer_answer"),
        ("quizzes", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quizquestion",
            old_name="questions",
            new_name="question",
        ),
        migrations.AlterUniqueTogether(
            name="quizquestion",
            unique_together={("quiz", "question")},
        ),
    ]
