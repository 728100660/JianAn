# Generated by Django 3.0.7 on 2020-07-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestnotify',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notify',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
