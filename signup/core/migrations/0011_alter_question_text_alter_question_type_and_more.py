# Generated by Django 4.0.5 on 2022-06-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_question_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=2550),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('char_field', 'char_field'), ('text_field', 'text_field')], default='text_field', max_length=255),
        ),
        migrations.AlterField(
            model_name='submission',
            name='answer',
            field=models.TextField(max_length=2550),
        ),
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', max_length=2550),
        ),
    ]
