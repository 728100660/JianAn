# Generated by Django 3.0.4 on 2020-10-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0020_auto_20201020_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpath',
            name='publicKey',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
