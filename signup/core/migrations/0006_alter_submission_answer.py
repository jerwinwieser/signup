# Generated by Django 4.0.5 on 2022-06-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_question_text_alter_submission_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='answer',
            field=models.TextField(max_length=2500),
        ),
    ]
