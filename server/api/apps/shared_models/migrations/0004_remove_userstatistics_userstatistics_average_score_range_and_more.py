# Generated by Django 4.0.6 on 2022-07-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared_models', '0003_alter_quizstatistics_options_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='userstatistics',
            name='UserStatistics_average_score_range',
        ),
        migrations.RemoveField(
            model_name='userstatistics',
            name='average_score',
        ),
    ]
