# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Api(models.Model):
    ke = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'API'


class Buildinfo(models.Model):
    place = models.CharField(max_length=10, blank=True, null=True)
    src = models.CharField(max_length=200, blank=True, null=True)
    floor = models.CharField(max_length=3, blank=True, null=True)
    index_i = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BuildInfo'


class Classroom(models.Model):
    classroom = models.CharField(max_length=10, blank=True, null=True)
    build = models.CharField(max_length=10, blank=True, null=True)
    day = models.CharField(max_length=5, blank=True, null=True)
    class1_2 = models.IntegerField(blank=True, null=True)
    class3_4 = models.IntegerField(blank=True, null=True)
    class5_6 = models.IntegerField(blank=True, null=True)
    class7_8 = models.IntegerField(blank=True, null=True)
    class9_11 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClassRoom'


class Classroomnumber(models.Model):
    place = models.CharField(max_length=10, blank=True, null=True)
    real_time_number = models.IntegerField(blank=True, null=True)
    max_people = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ClassroomNumber'


class CloudVideos(models.Model):
    mid = models.CharField(max_length=50)
    ke = models.CharField(max_length=50, blank=True, null=True)
    href = models.TextField()
    size = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cloud Videos'


class Events(models.Model):
    ke = models.CharField(max_length=50, blank=True, null=True)
    mid = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    time = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Events'


class Files(models.Model):
    ke = models.CharField(max_length=50)
    mid = models.CharField(max_length=50)
    name = models.TextField()
    size = models.FloatField()
    details = models.TextField()
    status = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Files'


class Latestnotify(models.Model):
    publisher = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=10, blank=True, null=True)
    release_time = models.DateTimeField()
    content = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LatestNotify'


class Logs(models.Model):
    ke = models.CharField(max_length=50, blank=True, null=True)
    mid = models.CharField(max_length=50, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Logs'


class Monitors(models.Model):
    mid = models.CharField(max_length=50, blank=True, null=True)
    ke = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    shto = models.TextField(blank=True, null=True)
    shfr = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    ext = models.CharField(max_length=50, blank=True, null=True)
    protocol = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    fps = models.IntegerField(blank=True, null=True)
    mode = models.CharField(max_length=15, blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    stoptime = models.CharField(max_length=20)
    starttime = models.CharField(max_length=20)
    enable = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'Monitors'


class Notify(models.Model):
    publisher = models.ForeignKey('User', models.DO_NOTHING, db_column='publisher', blank=True, null=True)
    title = models.CharField(max_length=6, blank=True, null=True)
    place = models.CharField(max_length=6, blank=True, null=True)
    release_time = models.DateTimeField()
    content = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Notify'


class Placeinfo(models.Model):
    place = models.CharField(max_length=10, blank=True, null=True)
    service = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaceInfo'


class Placenumber(models.Model):
    place = models.CharField(max_length=10, blank=True, null=True)
    real_time_number = models.IntegerField(blank=True, null=True)
    max_people = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    administrators = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlaceNumber'


class Presets(models.Model):
    ke = models.CharField(max_length=50, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Presets'


class Schedules(models.Model):
    ke = models.CharField(max_length=50, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    start = models.CharField(max_length=10, blank=True, null=True)
    end = models.CharField(max_length=10, blank=True, null=True)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Schedules'


class Schoolhospitalappointment(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    symptom = models.CharField(max_length=15, blank=True, null=True)
    time = models.DateTimeField()
    state = models.CharField(max_length=2, blank=True, null=True)
    version = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SchoolHospitalAppointment'


class TimelapseFrames(models.Model):
    ke = models.CharField(max_length=50)
    mid = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    filename = models.CharField(max_length=50)
    time = models.DateTimeField(blank=True, null=True)
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Timelapse Frames'


class Timelapses(models.Model):
    ke = models.CharField(max_length=50)
    mid = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.DateTimeField()
    end = models.DateTimeField()
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Timelapses'


class User(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    identity_id = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    authority = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=5, blank=True, null=True)
    classes = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    academy = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=15, blank=True, null=True)
    school = models.CharField(max_length=15, blank=True, null=True)
    src = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Users(models.Model):
    ke = models.CharField(max_length=50, blank=True, null=True)
    uid = models.CharField(max_length=50, blank=True, null=True)
    auth = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(unique=True, max_length=100, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'


class Videos(models.Model):
    mid = models.CharField(max_length=50, blank=True, null=True)
    ke = models.CharField(max_length=50, blank=True, null=True)
    ext = models.CharField(max_length=4, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    frames = models.IntegerField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Videos'


class Detector(models.Model):

    class Meta:
        managed = False
        db_table = 'detector'