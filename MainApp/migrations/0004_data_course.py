# Generated by Django 5.0.4 on 2024-06-13 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.course'),
        ),
    ]
