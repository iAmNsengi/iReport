# Generated by Django 5.0.4 on 2024-06-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_data_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='cat1',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='data',
            name='cat2',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='data',
            name='fat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='data',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
