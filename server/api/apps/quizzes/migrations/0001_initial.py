# Generated by Django 4.0.6 on 2022-11-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=200, unique=True)),
                ('answer', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('General', 'General'), ('Science', 'Science'), ('Maths', 'Maths'), ('History', 'History'), ('Geography', 'Geography'), ('Art', 'Art'), ('Literature', 'Literature'), ('Computer Science', 'Computer Science'), ('Business', 'Business'), ('Engineering', 'Engineering'), ('Medicine', 'Medicine')], default='General', max_length=100)),
                ('attempts', models.IntegerField(default=0)),
                ('correct', models.IntegerField(default=0)),
            ],
        ),
    ]
