# Generated by Django 4.0.5 on 2022-06-15 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_submission_bash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='bash',
            field=models.CharField(default='0123456789', max_length=10),
        ),
    ]