# Generated by Django 3.0.7 on 2020-07-15 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20200715_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='student_number',
            new_name='identity_id',
        ),
    ]