# Generated by Django 4.0.6 on 2022-07-24 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared_models', '0002_quizstatistics_userstatistics_quiztag_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizstatistics',
            options={'verbose_name_plural': 'Quiz statistics'},
        ),
        migrations.AlterModelOptions(
            name='userstatistics',
            options={'verbose_name_plural': 'User statistics'},
        ),
    ]
