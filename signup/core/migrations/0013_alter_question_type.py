# Generated by Django 4.0.5 on 2022-06-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_survey_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('CharField', 'CharField'), ('TextField', 'TextField')], default='TextField', max_length=255),
        ),
    ]
