from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    identity_id = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    authority = models.CharField(max_length=1, blank=True, null=True, default=1)
    name = models.CharField(max_length=5, blank=True, null=True)
    classes = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    academy = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=10, blank=True, null=True)
    school = models.CharField(max_length=15, blank=True, null=True)
    src = models.CharField(max_length=200, blank=True, null=True)
    openid = models.CharField(max_length=20, blank=True, null=True)

# 用户信息表
# class UserInfo(models.Model):
#     id = models.ForeignKey('User',
#                              models.DO_NOTHING,
#                              db_column='ID',
#                              primary_key=True)
#     name = models.CharField(max_length=5, blank=True, null=True)
#     classes = models.CharField(max_length=20, blank=True, null=True)
#     sex = models.CharField(max_length=1, blank=True, null=True)
#     academy = models.CharField(max_length=20, blank=True, null=True)

# 场所人数表
class PlaceNumber(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    place = models.CharField(max_length=10,blank=True, null=True)
    real_time_number = models.IntegerField(blank=True, null=True)
    max_people = models.IntegerField(blank=True, null=True)
    state = models.BooleanField(default=True)
    administrators = models.CharField(max_length=10,blank=True,null=True)

# test
class test(models.Model):
    name = models.CharField(max_length=10,blank=True, null=True)
    name1 = models.CharField(max_length=10,blank=True, null=True)
# 场所信息表
class PlaceInfo(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    place = models.CharField(max_length=10,blank=True, null=True)
    service = models.CharField(max_length=10, blank=True, null=True)

# 通知表
class Notify(models.Model):
    # publisher = models.CharField(max_length=10, blank=True, null=True)
    id = models.AutoField(db_column='id',
                          primary_key=True)
    publisher = models.ForeignKey('User',
                             models.DO_NOTHING,
                             db_column='publisher')

    # place = models.ForeignKey('PlaceInfo',
    #                          models.DO_NOTHING,
    #                          db_column='Place',
    #                          primary_key=True)
    place = models.CharField(max_length=10,blank=True, null=True)
    title = models.CharField(max_length=10,blank=True, null=True)
    release_time = models.DateField(blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)

# 教室表
class ClassRoom(models.Model):
    classroom = models.CharField(max_length=10,primary_key=True)
    build = models.CharField(max_length=10, blank=True, null=True)
    day = models.CharField(max_length=5, blank=True, null=True)
    class1_2 = models.BooleanField(default=False)
    class3_4 = models.BooleanField(default=False)
    class5_6 = models.BooleanField(default=False)
    class7_8 = models.BooleanField(default=False)
    class9_11 = models.BooleanField(default=False)


# 学校医院预约信息表
class SchoolHospitalAppointment(models.Model):
    # id = models.ForeignKey('User',
    #                          models.DO_NOTHING,
    #                          db_column='ID',
    #                          primary_key=True)
    user_id = models.ForeignKey('User',
                             models.DO_NOTHING,
                             db_column='user_id')
    symptom = models.CharField(max_length=200, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    version = models.CharField(max_length=4, blank=True, null=True)
    

# 建筑信息表
class BuildInfo(models.Model):
    # id = models.ForeignKey('User',
    #                          models.DO_NOTHING,
    #                          db_column='ID',
    #                          primary_key=True)
    place = models.CharField(max_length=15, blank=True, null=True)
    src = models.CharField(max_length=100, blank=True, null=True)
    floor = models.CharField(max_length=3, blank=True, null=True)
    index = models.CharField(max_length=4, blank=True, null=True)



# 教室人数表
class ClassroomNumber(models.Model):
    place = models.CharField(max_length=10,blank=True, null=True)
    real_time_number = models.IntegerField(blank=True, null=True)
    max_people = models.IntegerField(blank=True, null=True)
    state = models.BooleanField(default=True)


# 各个管理员的最新版本的通知表
class LatestNotify(models.Model):
    id = models.AutoField(db_column='id',
                          primary_key=True)
    publisher = models.ForeignKey('User',
                             models.DO_NOTHING,
                             db_column='publisher')

    # place = models.ForeignKey('PlaceInfo',
    #                          models.DO_NOTHING,
    #                          db_column='Place',
    #                          primary_key=True)
    place = models.CharField(max_length=10,blank=True, null=True)
    title = models.CharField(max_length=10,blank=True, null=True)
    release_time = models.DateField(blank=True, null=True)
    content = models.CharField(max_length=200, blank=True, null=True)


# 各个场所人流量表
class Stream_of_people(models.Model):
    place = models.CharField(max_length=10,blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    real_number = models.IntegerField(blank=True, null=True)
    max_number = models.IntegerField(blank=True, null=True)
    max_stage = models.IntegerField(blank=True, null=True)
    # six = models.IntegerField(blank=True, null=True, default=0)
    seven = models.IntegerField(blank=True, null=True, default=0)
    # eight = models.IntegerField(blank=True, null=True, default=0)
    nine = models.IntegerField(blank=True, null=True, default=0)
    # ten = models.IntegerField(blank=True, null=True, default=0)
    eleven = models.IntegerField(blank=True, null=True, default=0)
    # twelve = models.IntegerField(blank=True, null=True, default=0)
    thirteen = models.IntegerField(blank=True, null=True, default=0)
    # fourteen = models.IntegerField(blank=True, null=True, default=0)
    fifteen = models.IntegerField(blank=True, null=True, default=0)
    # sixteen = models.IntegerField(blank=True, null=True, default=0)
    seventeen = models.IntegerField(blank=True, null=True, default=0)
    # eighteen = models.IntegerField(blank=True, null=True, default=0)
    nineteen = models.IntegerField(blank=True, null=True, default=0)
    # twenty = models.IntegerField(blank=True, null=True, default=0)
    twenty_one = models.IntegerField(blank=True, null=True, default=0)