# Generated by Django 3.0.7 on 2020-07-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_auto_20200715_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='openid',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='src',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
