# Generated by Django 4.0.5 on 2022-06-13 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='question',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='core.question'),
        ),
    ]
