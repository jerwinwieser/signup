# Generated by Django 4.0.5 on 2022-06-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='test',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
