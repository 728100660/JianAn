# Generated by Django 3.0.7 on 2020-07-15 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20200715_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='publisher',
            field=models.ForeignKey(db_column='publisher', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='MyApp.User'),
        ),
    ]
