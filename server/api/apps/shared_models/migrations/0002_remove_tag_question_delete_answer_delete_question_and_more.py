# Generated by Django 4.0.6 on 2022-07-16 07:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shared_models", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tag",
            name="question",
        ),
        migrations.DeleteModel(
            name="Answer",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
