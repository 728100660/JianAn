# Generated by Django 3.0.7 on 2020-07-18 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20200718_0859'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='buildinfo',
            table='BuildInfo',
        ),
        migrations.AlterModelTable(
            name='classroom',
            table='ClassRoom',
        ),
        migrations.AlterModelTable(
            name='classroomnumber',
            table='ClassroomNumber',
        ),
        migrations.AlterModelTable(
            name='latestnotify',
            table='LatestNotify',
        ),
        migrations.AlterModelTable(
            name='notify',
            table='Notify',
        ),
        migrations.AlterModelTable(
            name='placeinfo',
            table='PlaceInfo',
        ),
        migrations.AlterModelTable(
            name='placenumber',
            table='PlaceNumber',
        ),
        migrations.AlterModelTable(
            name='schoolhospitalappointment',
            table='SchoolHospitalAppointment',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
