# Generated by Django 4.0.5 on 2022-06-12 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_submission_status_remove_submission_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='email',
        ),
    ]