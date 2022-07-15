# Generated by Django 4.0.5 on 2022-07-15 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_take', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MC', 'Multiple Choice'), ('SA', 'Short Answer')], default='MC', max_length=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time_limit',
            field=models.DurationField(default=datetime.timedelta(seconds=300)),
        ),
    ]
