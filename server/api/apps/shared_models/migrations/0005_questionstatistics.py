# Generated by Django 4.0.6 on 2022-07-24 12:14

import django.db.models.deletion
from django.db import migrations, models

a = "0004_remove_userstatistics_userstatistics_average_score_range_and_more"


class Migration(migrations.Migration):
    dependencies = [
        (
            "shared_models",
            a,
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="QuestionStatistics",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shared_models.question",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Question statistics",
            },
        ),
    ]