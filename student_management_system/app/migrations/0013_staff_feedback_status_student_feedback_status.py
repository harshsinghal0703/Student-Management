# Generated by Django 4.2.1 on 2023-06-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_student_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student_feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
