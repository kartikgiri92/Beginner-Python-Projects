# Generated by Django 2.1.1 on 2018-09-22 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='qno',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizTable', verbose_name='QUIZ NUMBER'),
        ),
    ]
