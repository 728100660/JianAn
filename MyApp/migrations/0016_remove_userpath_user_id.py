# Generated by Django 3.0.4 on 2020-08-20 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0015_auto_20200817_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpath',
            name='user_id',
        ),
    ]
