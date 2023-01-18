# Generated by Django 4.0.6 on 2022-12-29 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_rename_questions_quizquestion_question_and_more'),
        ('shared_models', '0005_questionresponse_attempt_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionresponse',
            name='attempt_id',
        ),
        migrations.RemoveField(
            model_name='questionresponse',
            name='date_submitted',
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz'),
        ),
    ]
