# Generated by Django 5.0.4 on 2024-06-12 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_alter_course_code_alter_course_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default='0', max_length=10),
        ),
    ]