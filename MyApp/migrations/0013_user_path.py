# Generated by Django 3.0.4 on 2020-08-17 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_auto_20200725_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(blank=True, null=True)),
                ('x', models.FloatField()),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.DO_NOTHING, to='MyApp.User')),
            ],
        ),
    ]
