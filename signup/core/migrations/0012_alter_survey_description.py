# Generated by Django 4.0.5 on 2022-06-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_question_text_alter_question_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='description',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit.', max_length=2550),
        ),
    ]