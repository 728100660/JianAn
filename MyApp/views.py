from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, PlaceInfo, PlaceNumber, Notify, ClassRoom, SchoolHospitalAppointment, BuildInfo, ClassroomNumber, LatestNotify
from .models import Stream_of_people, Temp, UserPath
import time
import datetime
from .common import merge_dict_list, unix_to_datetime, make_stage_number_for_dict,get_number_stage,tongtai_encrypt,make_room,decode

import random
import re
import os
from django.db.models import Sum, Max
import os
# Create your views here.


def make_path(request):
    paths = [[112.924665, 28.228095, 112.923767, 28.228143, 112.92383, 28.227912, 112.924225, 28.227848, 112.924315,
              28.225024, 112.924585, 28.224626, 112.926094, 28.224753, 112.926157, 28.22461, 112.926615, 28.224618],
             [112.926741, 28.22749, 112.927136, 28.227498, 112.927073, 28.227618, 112.926381, 28.227713, 112.926309, 28.227872,
              112.925654, 28.227896, 112.925366, 28.227785, 112.925591, 28.227228, 112.924917, 28.227005, 112.924935, 28.226806, 112.925124, 28.226822],
             [112.927962, 28.223774, 112.927387, 28.22379, 112.92719, 28.224809, 112.924567, 28.224626, 112.924674, 28.224355, 112.924863, 28.224459]]
    user_names = ['jjk', '王小明', '李小勇']
    t_time = int(time.time())
    for index, path in enumerate(paths):
        n = len(path)
        i = 0
        user_name = user_names[index]
        while(i < n):
            lng = path[i]
            i += 1
            lat = path[i]
            i += 1
            p = UserPath(lat=lat, lng=lng, name=user_name, time=t_time)
            try:
                p.save()
                print({'data': '存储路径成功', 'code': 1})
            except Exception as e:
                print(e)
                return JsonResponse({'data': '存储路径失败', 'code': 0})
    return JsonResponse({'data': '存储路径成功', 'code': 1})


def change(request):
    indexs = {'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1',
              'D2', 'D3'}
    places = ['贤德书院', '萃雅书院', '陌陌书院', '贤德食堂', '萃雅食堂',
              '楚枫轩食堂', '岭南食堂', '咸嘉食堂', '至诚楼', '日新楼', '乐知楼', '博学楼', '图书馆']
    # for index in indexs:
    # places = Stream_of_people.objects.filter(place='cfsy').values()
    # for place in places:
    ps = Stream_of_people.objects.filter(max_number=100).values()
    for p in ps:
        p = Stream_of_people.objects.filter(pk=p['id']).get()
        # p.max_number = random.randint(80, 100)
        p.max_number = random.randint(80, 100)
        p.save()
    return HttpResponse('更改成功')


def test(request):
    return JsonResponse([1, 2, 3], safe=False)
    # data = User.objects.filter(name='pxz').aggregate(Max('id'))
    # user_infor = User.objects.filter(name='pxz').values()
    # return JsonResponse({'user_info':list(user_infor)})
    # print(data)
    # data = User.objects.filter(name='pxz').get()
    # result = [data]
    # return JsonResponse(list(result),safe=False)
    # 获取当前工作路径
    # pwd = os.getcwd()
    # pwd =  os.getcwd()+'/static/'+'55664'+'.png'
    # print(type(pwd),pwd)
    # pwd = pwd.split('\\')
    # print(type(pwd),pwd)
    # pwd = '/'.join(pwd)
    # print(type(pwd),pwd)
    # return HttpResponse('asdf')

    # for i in range(1172,1206):
    #     date = datetime.datetime.now()
    #     place = Stream_of_people.objects.filter(pk=i).get()
    #     place.date = date
    #     place.save()

    # 初始化各个场所人流量
    rooms = {'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1',
             'D2', 'D3'}
    date = datetime.datetime.now()
    # 更改日期为昨天
    # date = date + datetime.timedelta(days=-1)
    for room in rooms:
        for i in range(10):
            i += 1
            if i < 10:
                temp_room = room+'0'+str(i)
            else:
                temp_room = room+str(i)
            place = Stream_of_people(place=temp_room, date=date, real_number=random.randint(0, 80), max_number=random.randint(80, 100),
                                     max_stage=10, seven=random.randint(0, 80), nine=random.randint(0, 80),
                                     eleven=random.randint(0, 80), thirteen=random.randint(0, 80),
                                     fifteen=random.randint(0, 80), seventeen=random.randint(0, 80),
                                     nineteen=random.randint(0, 80), twenty_one=random.randint(0, 80), capacity=100)
            place.save()
    places = ['校医院', '贤德书院', '萃雅书院', '陌陌书院', '贤德食堂', '萃雅食堂',
              '楚枫轩食堂', '岭南食堂', '咸嘉食堂', '至诚楼', '日新楼', '乐知楼', '博学楼', '图书馆']
    for place in places:
        place = Stream_of_people(place=place, date=date, real_number=random.randint(0, 800), max_number=random.randint(800, 1000),
                                 max_stage=10, seven=random.randint(0, 800), nine=random.randint(0, 800),
                                 eleven=random.randint(0, 800), thirteen=random.randint(0, 800),
                                 fifteen=random.randint(0, 800), seventeen=random.randint(0, 800),
                                 nineteen=random.randint(0, 800), twenty_one=random.randint(0, 800), capacity=1000)
        place.save()
    return HttpResponse('成功')
    # 初始化教室人数表
    # rooms = {'A1','B1','C1','D1','A2','B2','C2','D2','A3','B3','C3','D3'}
    # for room in rooms:
    #     for i in range(10):
    #         i+=1
    #         if i < 10:
    #             temp_room = room+'0'+str(i)
    #         else:
    #             temp_room = room+str(i)
    #         place = ClassroomNumber(place=temp_room,real_time_number=i*5,max_people=i*10,state=1)
    #         place.save()
    # return HttpResponse('成功')

    # 初始化区域人数表
    # places = ['校医院', '贤德书院', '萃雅书院', '陌陌书院', '贤德食堂', '萃雅食堂',
    #           '楚枫轩食堂', '岭南咸嘉食堂', '至诚楼', '日新楼', '乐知楼', '博学楼', '图书馆']
    # for place in places:
    #     place = PlaceNumber(place=place, real_time_number=11,
    #                         max_people=100, state=1, administrators=1)
    #     place.save()
    return HttpResponse('添加成功')


def change_stream_of_people(request):
    # 造数据！
    if request.GET:
        if request.GET.get('flag') == '1':
            places = ['校医院', '贤德书院', '萃雅书院', '陌陌书院', '贤德食堂', '萃雅食堂',
                    '楚枫轩食堂', '岭南食堂', '咸嘉食堂', '至诚楼', '日新楼', '乐知楼', '博学楼', '图书馆']
            date = datetime.datetime.now()
            for i in range(31):
                temp = date
                tpDate = -i # 偏移日期量
                temp = date + datetime.timedelta(days=tpDate)
                temp = temp.strftime('%Y-%m-%d')
                for place in places:
                    print(f'============正在修改{temp}时间的{place}场所=============')
                    streamInfo = Stream_of_people.objects.filter(place=place,date = temp).get()
                    capacity = streamInfo.capacity
                    tpStreamDict = make_stage_number_for_dict(streamInfo.place, capacity)
                    print(tpStreamDict)
                    streamInfo.seven = tpStreamDict['seven']
                    streamInfo.nine = tpStreamDict['nine']
                    streamInfo.eleven = tpStreamDict['eleven']
                    streamInfo.thirteen = tpStreamDict['thirteen']
                    streamInfo.fifteen = tpStreamDict['fifteen']
                    streamInfo.seventeen = tpStreamDict['seventeen']
                    streamInfo.nineteen = tpStreamDict['nineteen']
                    streamInfo.twenty_one = tpStreamDict['twenty_one']
                    maxNumber = max(tpStreamDict.values())
                    streamInfo.max_number = maxNumber
                    for key in tpStreamDict:
                        if tpStreamDict[key]==maxNumber:
                            num = get_number_stage(key)
                            max_stage = num
                            break
                    streamInfo.real_number = tpStreamDict['real_number']
                    streamInfo.max_stage = max_stage
                    streamInfo.save()
                    print(f'修改{temp}时间的{place}场所成功')
                    print('=========')
            return HttpResponse('全部修改成功！')
        return HttpResponse('do nothing')
    return HttpResponse('方法错误')

        


def make_data_for_classroomnumber(request):
    # 造教室里面的数据
    if request.GET:
        flag = request.GET.get('flag')
        a = locals()
        print(a)
        if flag == '1':
            rooms = {'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1',
                     'D2', 'D3'}
            max_people = [80, 80]
            for room in rooms:
                for i in range(10):
                    i += 1
                    if i < 10:
                        temp_room = room+'0'+str(i)
                    else:
                        temp_room = room+str(i)
                    print(temp_room)
                    index = random.randint(0, 1)
                    number = random.randint(5, 50)
                    place = ClassroomNumber(
                        place=temp_room, real_time_number=number, max_people=max_people[index], state=1)
                    place.save()
            return HttpResponse('ok')
        return HttpResponse('do nothing')
    return HttpResponse('get nothing')

# 注册账户信息


def register(request):
    password = '123456'
    authority = '1'
    phone_number = '234526721'
    identity_id = '123526712'
    name = 'pxz'
    academy = '计算机与信息工程学院'
    classes = '1'
    sex = '0'
    major = '物联'
    school = '湖南工商大学'
    user = User(password=password, authority=authority,
                phone_number=phone_number, identity_id=identity_id, name=name, academy=academy, classes=classes, sex=sex, major=major, school=school)
    if User.objects.filter(phone_number=phone_number).exists():
        return HttpResponse('该手机号码已经注册过账户了')
    elif User.objects.filter(identity_id=identity_id).exists():
        return HttpResponse('该学号已经注册过账户了！')
    try:
        user.save()
    except Exception as e:
        print(e)
        return HttpResponse('error')
    return HttpResponse('success!')

# 绑定学号对应的学生信息


def bind(request):
    if request.POST:
        phone_number = request.POST.get('phone_number')
        school = request.POST.get('school')
        name = request.POST.get('name')
        identity_id = request.POST.get('identity_id')
        src = request.POST.get('src')
        openid = request.POST.get('openid')
        # phone_number = '12345672'
        # identity_id = '12345672'
        if User.objects.filter(phone_number=phone_number).exists():
            # data = User.objects.filter(phone_number=phone_number).values()
            return JsonResponse({'data': '该微信账号已被绑定', 'code': 0})
        else:
            try:
                data = User.objects.filter(
                    identity_id=identity_id, school=school, name=name).get()
            except Exception as e:
                print(e)
                return JsonResponse({'data': '学生信息有误', 'code': 0})
            if data.phone_number:
                return JsonResponse({'data': '该学生已被绑定', 'code': 0})
            else:
                data.openid = openid
                data.phone_number = phone_number
                data.src = src
                data.save()
                return JsonResponse({'data': [{'user_id': data.pk}], 'code': 1})

# 登录


def login(request):
    if request.POST:
        school = request.POST.get('school')
        identity_id = request.POST.get('identity_id')
        password = request.POST.get('password')
        if User.objects.filter(school=school, identity_id=identity_id).exists():
            user = User.objects.filter(
                school=school, identity_id=identity_id).get()
            if user.password == password:
                data = [{'user_id': user.pk, 'authority': user.authority}]
                return JsonResponse({'data': data, 'code': 1})
            return JsonResponse({'data': '用户密码输入错误 ', 'code': 0})
        else:
            return JsonResponse({'data': '学校或学工号信息有误', 'code': 0})
    return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})
# 登录
# def login(request):
#     phone_number = '12345678'
#     identity_id = '1234567'
#     password = '123456'
#     if User.objects.filter(phone_number=phone_number).exists():
#         users = User.objects.filter(phone_number=phone_number)
#         # if user.password == password:
#         # return HttpResponse('登录成功')
#         # 怎么不通过for循环访问user里面的数据？
#         for user in users:
#             if user.password == password:
#                 return HttpResponse('登录成功')
#             else:
#                 return HttpResponse('defeat')
#     elif User.objects.filter(identity_id=identity_id).exists():
#         users = User.objects.filter(identity_id=identity_id)
#         for user in users:
#             if user.password == password:
#                 return HttpResponse('登录成功')
#             else:
#                 return HttpResponse('defeat')
#     else:
#         return HttpResponse('账号错误')


# 登录
# def login(request):
#     if request.POST:
#         phone_number = request.POST.get('phone_number')
#         school = request.POST.get('school')
#         identity_id = request.POST.get('identity_id')
#         # phone_number = '12345672'
#         if User.objects.filter(phone_number=phone_number).exists():
#             data = User.objects.filter(phone_number=phone_number).values()
#             if data[0]['identity_id']==identity_id:
#                 return JsonResponse({'data':list(data),'code':1})
#             else:
#                 return JsonResponse({'data':'手机号码与学号不一致','code':0})
#         else:
#             data = User.objects.filter(identity_id=identity_id).get()
#             if data.phone_number:
#                 return JsonResponse({'data':'手机号码与学号不一致','code':0})
#             else:
#                 data.phone_number = phone_number
#                 data.save()
#             data = User.objects.filter(phone_number=phone_number).values()
#             return JsonResponse({'data':list(data),'code':1})
    #     return JsonResponse({'data':data,'code':1})
    # return JsonResponse({'data':'请先绑定学生信息','code':0})


# 获取场所人数
def get_number(request):
    if request.GET:
        place = request.GET.get('place')
        flag = request.GET.get('flag')
        floor = request.GET.get('floor')
        # 如果有flag就将PlaceNumber表中所有数据返回
        if flag:
            placenumber = PlaceNumber.objects.all().values()
        elif floor:
            # 如果有floor的数据就是请求教学楼中具体的层数，当前层所有教室，的人数
            indexs = BuildInfo.objects.filter(place=place).values('index')
            print(indexs)
            indexs = indexs[0]['index'].split('_')
            result = []
            print(indexs)
            for index in indexs:
                # temp=A1,A2,B2之类的
                temp_index = index+floor
                data = ClassroomNumber.objects.filter(
                    place__contains=temp_index).values()
                result += data
            return JsonResponse({'data': result, 'code': 1})
        else:
            placenumber = PlaceNumber.objects.filter(
                place__contains=place).values()
        return JsonResponse({'data': list(placenumber), 'code': 1})


# 获取用户信息
# 后期完善
# get请求方式id
def get_user_info(request):
    if request.GET:
        id = request.GET.get('user_id')
        # id = '1'
        user = User.objects.filter(pk=id).values(
            'name', 'school', 'authority', 'src', 'major', 'classes', 'academy', 'sex', 'identity_id')
        # 返回格式
        # {user：[{}{}{}{}]}
        return JsonResponse({'data': list(user), 'code': 1})

# 修改个人信息
# 后期完善
# change（忘记专业术语了）请求方式


def modify_information(request):
    return JsonResponse({'code': 1})

# 发布通知


def sent_notify(request):
    print(request)
    print(request.POST)
    print(request.POST.get('user_id'))
    print(request.POST.get('title'))
    if request.POST:
        title = request.POST.get('title')
        content = request.POST.get('content')
        id = request.POST.get('user_id')
        print(request.POST, id, type(id))
        # place = request.POST.get('place')
        # title = 'title'
        # content = 'contentyyy'
        # id = '2'
        user = User.objects.filter(pk=id).get()
        print(user.pk)
        # authority = user.authority
        release_time = datetime.datetime.now()
        # temp_place = PlaceNumber.objects.filter(place=place).get()
        # if authority == '0'::
        #     # print(temp_place.state)
        '''publisher关联了user，这里赋值要注意'''
        notify = Notify(title=title, publisher=user,
                        release_time=release_time, content=content)
        try:
            notify.save()
        except Exception as e:
            print(e)
            return JsonResponse({'data': '发布通知失败!', 'code': 0})
        # 如果该用户之前发过通知，则将其在LatestNotify表中的信息更新
        # 否则在LatestNotify表中新建一条数据
        if LatestNotify.objects.filter(publisher=user).exists():
            notify = LatestNotify.objects.filter(publisher=user).get()
            notify.title = title
            notify.release_time = release_time
            notify.content = content
            try:
                notify.save()
            except Exception as e:
                print(e)
                return({'data': '发布通知成功，但是更新信息失败', 'code': 1})
        else:
            notify = LatestNotify(
                title=title, publisher=user, release_time=release_time, content=content)
            try:
                notify.save()
            except Exception as e:
                print(e)
                return({'data': '发布通知成功，但是更新信息失败', 'code': 1})
        return JsonResponse({'data': '发布通知成功!', 'code': 1})

        # elif temp_place.administrators == authority:
        #     notify = Notify(place=place,title=title,publisher=id,release_time=release_time)
        #     try:
        #         notify.save()
        #     except Exception as e:
        #         print(e)
        #         return JsonResponse({'data':'发布通知失败!','code':0})
        #     return JsonResponse({'data':'发布通知成功!','code':1})
        # else:
        #     return JsonResponse({'data':'没有权限!','code':0})

        # if id == '1':
        #     return JsonResponse({'code':0})

        # elif id == '2':
        #     place = '图书馆'
        #     notify = Notify(place=place,title=title,publisher=id,release_time=release_time)
        #     try:
        #         notify.save()
        #     except Exception as e:
        #         print(e)
        #         return JsonResponse({'code':0})
        #     return JsonResponse({'code':1})
        # elif id == '3':
        #     place = '食堂'
        #     notify = Notify(place=place,title=title,publisher=id,release_time=release_time)
        #     try:
        #         notify.save()
        #     except Exception as e:
        #         print(e)
        #         return JsonResponse({'code':0})
        #     return JsonResponse({'code':1})
        # elif id == '4':
        #     place = '书院'
        #     notify = Notify(place=place,title=title,publisher=id,release_time=release_time)
        #     try:
        #         notify.save()
        #     except Exception as e:
        #         print(e)
        #         return JsonResponse({'code':0})
        #     return JsonResponse({'code':1})
        # elif id == '0':
        #     # 此处place为学校，需要动态获取
        #     place = User.objects.filter(pk=id).valuse('school')
        #     notify = Notify(place=place,title=title,publisher=id,release_time=release_time)
        #     try:
        #         notify.save()
        #     except Exception as e:
        #         print(e)
        #         return JsonResponse({'code':0})
        #     return JsonResponse({'code':1})
        # return JsonResponse({'code':1})
    return JsonResponse({'data': '未使用POST方式传值，或者未传输数据到后台', 'code': 0})

# 设置场所状态
# 没做权限，数据库需要新增一张表，表记录权限id对应的地区


def set_status(request):
    if request.POST:
        places = request.POST.get('place')
        # print(places)
        # print(type(places))
        places = places.split(',')
        # print(type(places))
        # print(places)
        state = request.POST.get('state')
        id = request.POST.get('user_id')
        # id = '2'
        # place = '贤德书院'
        # state = 0
        user = User.objects.filter(pk=id).get()
        authority = user.authority
        # print(type(authority))
        for place in places:
            flag = 0
            print(place)
            print(type(place), place)
            if '至诚楼' in place:
                flag = 1
                rooms = make_room(['A1', 'A2', 'A3', 'B1', 'B2', 'B3'])
            if '日新楼' in place:
                flag = 1
                rooms = make_room(['C1', 'C2', 'C3', 'D1', 'D2', 'D3'])
            if '乐知楼' in place:
                flag = 1
                rooms = make_room(['E1', 'E2', 'E3', 'F1', 'F2', 'F3'])
            temp_place = PlaceNumber.objects.filter(place=place).get()
            # print('state',state==temp_place.state)
            if authority == '0':
                # print(temp_place.state)
                temp_place.state = state
                temp_place.save()
                try:
                    if flag:
                        for room in rooms:
                            c = ClassroomNumber.objects.filter(place=room).get()
                            c.state = state
                            c.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({'data':'未知错误', 'code':0})
            elif temp_place.administrators == authority:
                # print(temp_place.state)
                temp_place.state = state
                temp_place.save()
                try:
                    if flag:
                        for room in rooms:
                            c = ClassroomNumber.objects.filter(place=room).get()
                            c.state = state
                            c.save()
                except Exception as e:
                    print(e)
                    return JsonResponse({'data':'未知错误', 'code':0})
            else:
                return JsonResponse({'data': '没有权限!', 'code': 0})
            # try:
            #     temp_place = PlaceNumber.objects.filter(place=place).get()
            #     print(temp_place.state)
            #     temp_place.state=state
            #     temp_place.save()
            # except Exception as e:
            #     print(e)
            #     return JsonResponse({'code':0})
            return JsonResponse({'data': '成功', 'code': 1})
        return JsonResponse({'data': '失败，未接收到place数据', 'code': 0})
    return JsonResponse({'data': '失败，请求方式失败或未接受到任何传值，请用get方法传值', 'code': 0})


# 医院预约功能,预约时间不允许选择，预约完之后必须在15分钟之内到达校医院（即预约有效时间只有15分钟）
def appointment(request):
    if request.POST:
        user_id = request.POST.get('user_id')
        symptom = request.POST.get('symptom')
        state = request.POST.get('state')
        valid_period = 1
        now_time = datetime.datetime.now()
        time = now_time + datetime.timedelta(days=valid_period)
        print(time)
        # user_id = '1'
        # symptom = 'symptom'
        # state = '1'
        # time 是预约时间，不是当前时间
        # time = datetime.datetime.now()
        # 当前时间
        now_time = datetime.datetime.now()
        # user = User.objects.filter(pk=id).get()
        # 判断当前用户是否有有效预约在进行
        if SchoolHospitalAppointment.objects.filter(user_id=user_id, time__gt=now_time).exists():
            if state == '1':
                # 如果是预约请求的话
                # 您已经预约过一次了，请先取消预约
                return JsonResponse({'data': '你已经预约过一次了', 'code': 0})
            elif state == '3':
                # 如果是取消预约请求的话
                # 取消预约，预约人数减一
                try:
                    # 取消预约
                    hospital = SchoolHospitalAppointment.objects.filter(
                        user_id=user_id, time__gt=now_time, state='1').get()
                    hospital.state = '3'
                    hospital.save()
                    # 人数减一
                    number = Placenumber.objects.filter(place='校医院').get()
                    Placenumber = PlaceNumber(
                        real_time_number=number.real_time_number-1)
                    Placenumber.save()
                except Exception as e:
                    print(e, 1)
                    return JsonResponse({'code': 0})
                return JsonResponse({'data': '取消预约成功！', 'code': 0})
        else:
            # 没有预约的话就预约
            # 预约
            # 如果用户是以前就有预约信息在数据库，获取最大版本号且新建一条预约信息将版本号＋1，将医院预约人数+1
            if SchoolHospitalAppointment.objects.filter(user_id=user_id).exists():
                max_v = SchoolHospitalAppointment.objects.filter(
                    user_id=user_id).aggregate(Max('version'))
                print(max_v)
                user = User.objects.filter(pk=user_id).get()
                max_version = int(max_v['version__max'])
                hospital = SchoolHospitalAppointment(
                    user_id=user, symptom=symptom, state=state, time=time, version=str(max_version+1))
                number = PlaceNumber.objects.filter(place='校医院').get()
                # 人数+1
                number.real_time_number = str(number.real_time_number+1)
                number.save()
                hospital.save()
                # max_v['version__max'] = int(max_v['version__max'])+1
                # hospital = SchoolHospitalAppointment.objects.filter(version=max_v['version__max'],user_id=user_id).get()
                # hospital.version = str(int(hospital.version)+1)
                # hospital.save()
            else:
                # 如果以前没有预约信息，将其版本号置为1
                user = User.objects.filter(pk=user_id).get()
                hospital = SchoolHospitalAppointment(
                    user_id=user, symptom=symptom, state=state, time=time, version='1')
                # print(1)
                hospital.save()
                # print(2)
                # 人数加一
                number = PlaceNumber.objects.filter(place='校医院').get()
                # print(number.real_time_number)
                # print(type(number.real_time_number))
                number.real_time_number = str(number.real_time_number+1)
                number.save()
            # except Exception as e:
            #     print(e,2)
            #     return JsonResponse({'code':0})
            return JsonResponse({'data': '预约成功！', 'code': 1})
    return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


# 完成预约，此时预约人数减一，状态变为 0
def finish_appointment(request):
    if request.POST:
        user_id = request.POST.get('user_id')
    # user_id = '1'
        state = '0'
        place = '校医院'
        number = PlaceNumber.objects.filter(place=place).get()
        # if SchoolHospitalAppointment.objects.aggregate(Max('time')).filter(user_id=user_id).exists():
        # 判断当前用户是否预约
        # 如果已经预约，则完成预约
        if SchoolHospitalAppointment.objects.filter(user_id=user_id, time__gt=now_time).exists():
            max_v = SchoolHospitalAppointment.objects.filter(
                user_id=user_id).aggregate(Max('version'))
            user_appointment = SchoolHospitalAppointment.objects.filter(
                version=max_v['version__max'], user_id=user_id).get()
            # 更新信息，没必要将version+1
            # user_appointment.version = str(int(hospital.version)+1)
            user_appointment.state = state
            user_appointment.save()
            return JsonResponse({'data': '完成预约！', 'code': 1})
        else:
            return JsonResponse({'data': '该用户没有预约信息，无法完成预约', 'code': 0})
    return JsonResponse({'data': '请求方式错误', 'code': 0})


# 获取指定用户的预约信息
def get_appointment_info(request):
    if request.GET:
        user_id = request.GET.get('user_id')
        # now_time = time.time()
        # appointment_infos = SchoolHospitalAppointment.objects.filter(time__gt=now_time).values('symptom','user_id')
        # appointment_infos = SchoolHospitalAppointment.objects.filter(time__lt=now_time).values('symptom','user_id','state')
        appointment_infos = SchoolHospitalAppointment.objects.filter(
            user_id=user_id).values('symptom', 'user_id', 'state')
        # print(appointment_infos)
        data = []
        for appointment_info in appointment_infos:
            user = User.objects.filter(pk=appointment_info['user_id']).values(
                'id', 'identity_id', 'name')
            # print(user,appointment_info)
            # user是queryset，要转换成列表
            # 将两个[{}]合并成一个[{}]，并添加到返回列表中
            listmerge = list(user) + [appointment_info]
            print(listmerge)
            data += merge_dict_list(listmerge)
        return JsonResponse({'data': data, 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


# 获取所有通知内容
def get_notify(request):
    if request.method == 'GET':
        data = []
        user_id = request.GET.get('user_id')
        notifys = Notify.objects.all().values()
        for notify in notifys:
            print(notify)
            user = User.objects.filter(pk=notify['publisher_id']).values(
                'id', 'identity_id', 'name')
            listmerge = list(user) + [notify]
            data += merge_dict_list(listmerge)
        return JsonResponse({'data': data, 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误', 'code': 0})


# 获取当前用户所管理的区域
def get_place(request):
    if request.GET:
        # user_id = request.GET.get('user_id')
        authority = request.GET.get('authority')
        if authority == '0':
            places = PlaceNumber.objects.all().values()
        else:
            places = PlaceNumber.objects.filter(
                administrators=authority).values('place')
        return JsonResponse({'data': list(places), 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


# 获取教学楼信息ab=academybuild


def get_ab_info(request):
    if request.method == 'GET':
        places = BuildInfo.objects.all().values()
        return JsonResponse({'data': list(places), 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误', 'code': 0})


# 获取最新通知信息
def get_latest_notify(request):
    if request.method == 'GET':
        latest_notifys = LatestNotify.objects.all().values()
        data = []
        for latest_notify in latest_notifys:
            user = User.objects.filter(pk=latest_notify['id']).values('name')
            listmerge = list(user)+[latest_notify]
            data += merge_dict_list(listmerge)
        return JsonResponse({'data': list(data), 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误', 'code': 0})


# 上传文件
def upload_file(request):
    if request.POST:
        rec_file = request.FILES.get('icon')
        identity_id = request.POST.get('identity_id')
        # print(rec_file)
        # 获取当前工作路径
        # pwd =  os.getcwd()+'/static/'+identity_id+'.png'
        # linux路径和windows路径获取有点不一样
        suffix = str(int(time.time()))
        pwd = os.getcwd()+'/static/'+identity_id+suffix+'.png'
        pwd = pwd.split('\\')
        pwd = '/'.join(pwd)
        print(pwd)
        # with 在读取完毕后，自动关闭
        with open(pwd, 'wb') as save_file:
            for part in rec_file.chunks():
                save_file.write(part)
                save_file.flush()

        # 添加后缀,time.time是float类型的（精确到秒数下的小数点，把小数点后面的去掉），先转为int再转为str
        # suffix = str(int(time.time()))
        # 更新存储头像url的src
        src = 'https://www.jianan.site/static/'+identity_id+suffix+'.png'
        user = User.objects.filter(identity_id=identity_id).get()
        user.src = src
        user.save()
        data = [{'src': src}]
        return JsonResponse({'data': data, 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


# 获取各个地方的人流量数据
def get_stream_people(request):
    if request.GET:
        place = request.GET.get('place')
        date = datetime.datetime.now()
        if place == '校医院':
            dates, j, data = [], 0, []
            result, result2 = {}, {}
            for i in range(2):
                temp = date + datetime.timedelta(days=-i)
                dates.append(temp.strftime('%Y-%m-%d'))
            for date in dates:
                print('date',date)
                j += 1
                counts = PlaceNumber.objects.filter(
                    place='校医院').values('max_people')
                count = SchoolHospitalAppointment.objects.filter(
                    time=date).count()
                # number记录各个时间段校医院人数
                number = [0, 0, 0, 0, 0, 0, 0, 0]
                for i in range(count):
                    rand = random.randint(0, 7)
                    number[rand] += 1
                number.append(count)
                if j == 1:
                    result['校医院'] = number
                    result['capacity'] = counts[0]['max_people']
                else:
                    result2['校医院'] = number
                    result2['capacity'] = counts[0]['max_people']
                symptoms = {'呼吸困难': 0, '干咳': 0, '乏力': 0, '发烧': 0,'其它':0}
                for symptom in symptoms.keys():
                    num = SchoolHospitalAppointment.objects.filter(
                        symptom__contains=symptom, time=date).count()
                    symptoms[symptom] = num
                symptoms['count'] = count
                data.append(symptoms)
            return JsonResponse({'data': data, 'datalist': result, 'yesterdaylist': result2, 'code': 1})
        yesterday = date+datetime.timedelta(days=-1)
        date = date.strftime('%Y-%m-%d')
        yesterday = yesterday.strftime('%Y-%m-%d')
        print(date)
        indexs = ['书院', '食堂', '楼', '馆']
        stages = ['seven', 'nine', 'eleven', 'thirteen',
                  'fifteen', 'seventeen', 'nineteen', 'twenty_one']
        for index in indexs:
            if re.search(index, place):
                # 查询昨天的数据，进行对比
                yesterday_info = Stream_of_people.objects.filter(
                    place__contains=index, date=yesterday).values()
                place_info = Stream_of_people.objects.filter(
                    place=place, date=date).values()
                # yesterday_data存储昨日该区域（和与之相关的区域，如现在查询贤德食堂，相关区域就是其他食堂）每个时间段的人数，是一个{[]}，data则是存储当日每个时间段的人数
                data, temp, yesterday_data = 9*[0], 9*[0], {}
                for j in range(len(yesterday_info)):
                    i = 0
                    for stage in stages:
                        data[i] = place_info[0][stage]
                        temp[i] = yesterday_info[j][stage]
                        i += 1
                    key = yesterday_info[j]['place']
                    # 下标8代表昨日该场所总人流量
                    temp[8] = max(temp[:8])
                    yesterday_data[key] = temp.copy()
                # 下标8代表昨日该场所总人流量
                data[8] = max(data)
                return JsonResponse({'data': list(place_info), 'yesterdaylist': yesterday_data, 'datalist': {place: data}, 'code': 1})
        # 如果传过来的place都没有包含indexs里面的数据，说明就是查询教室里面的人数
        data, i, yesterday_data = 9*[0], 0, 9*[0]
        yesterday_info = Stream_of_people.objects.filter(
            place=place, date=yesterday).values()
        place_info = Stream_of_people.objects.filter(
            place=place, date=date).values()
        for stage in stages:
            print(place_info, date, place)
            data[i] = place_info[0][stage]
            yesterday_data[i] = yesterday_info[0][stage]
            i += 1
        yesterday_data[8] = max(yesterday_data)
        data[8] = max(data)
        return JsonResponse({'data': list(place_info), 'yesterdaylist': {place: yesterday_data}, 'datalist': {place: data}, 'code': 1})
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


# 获取七天内各个地方的人流量数据
def get_stream_people_week(request):
    if request.GET:
        place = request.GET.get('place')
        date = datetime.datetime.now()
        dates = []
        if place == '校医院':
            result = []
            for i in range(7):
                # 校医院预约表中，time=7-25表示的是7.24号的预约信息
                temp = date+datetime.timedelta(days=-i)
                dates.append(temp.strftime('%Y-%m-%d'))
            counts = []
            symptoms = {'呼吸困难': 0, '干咳': 0, '乏力': 0, '发烧': 0, '其他':0}
            for date in dates:
                # count是当天患者总人数
                # count = 0
                count = SchoolHospitalAppointment.objects.filter(
                    time=date).count()
                counts.append(count)
                for symptom in symptoms.keys():
                    num = SchoolHospitalAppointment.objects.filter(
                        symptom__contains=symptom, time=date).count()
                    symptoms[symptom] += num
            result.append(symptoms)
            return JsonResponse({'data': result, '校医院': counts})
        else:
            for i in range(7):
                temp = date+datetime.timedelta(days=-i-1)
                dates.append(temp.strftime('%Y-%m-%d'))
            indexs = ['书院', '食堂', '楼', '馆', '医院']
            stages = ['seven', 'nine', 'eleven', 'thirteen',
                      'fifteen', 'seventeen', 'nineteen', 'twenty_one']
            # result{'地点1':[1,2,66,113],'地点2'....}
            result = {}
            # for循环，按天数
            j = 0
            for date in dates:
                j += 1
                for index in indexs:
                    if re.search(index, place):
                        # 如果查询的是贤德书院，那么places中应该是所有书院的名字
                        places = PlaceNumber.objects.filter(
                            place__contains=index).values('place')
                        for t_place in places:
                            place_info = Stream_of_people.objects.filter(
                                place=t_place['place'], date=date).values('max_number')
                            # 如果result中没有当前场所的信息，则，新增该场所的key，key值是个存储了每天人数的列表，如果有则往列表
                            if t_place['place'] in result:
                                result[t_place['place']].append(
                                    place_info[0]['max_number'])
                            else:
                                print(place_info, date, t_place['place'])
                                result[t_place['place']] = [
                                    place_info[0]['max_number']]
                            if j == 7:
                                result[t_place['place']].append(
                                    sum(result[t_place['place']]))
            return JsonResponse(result)
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


# 获取警告信息
def warning_message(request):
    date = datetime.datetime.now()
    date = date.strftime('%Y-%m-%d')
    place_infos = Stream_of_people.objects.filter(date=date).values()
    # place_infos = PlaceNumber.objects.filter().values()
    result = []
    data = {}
    indexs = ['书院', '食堂', '楼', '馆', '医院']
    for place_info in place_infos:
        # print(place_info)
        if place_info['real_number'] >= place_info['capacity']:
            data['place'] = place_info['place']
            for index in indexs:
                if re.search(index, place_info['place']):
                    administrators = PlaceNumber.objects.filter(
                        place=place_info['place']).values('administrators')
                    # print(administrators)
                    data['administrators'] = administrators[0]['administrators']
                    break
                    # print(data)
                else:
                    data['administrators'] = '6'
            print(data)
            result.append(data.copy())
    # datas = Temp.objects.filter(is_delete=0).values()
    # for data in datas:
    #     d = Temp.objects.filter(place=data['place'],is_delete=0).get()
    #     d.is_delete=1
    #     d.save()
    return JsonResponse({'data': result, 'code': 1})


def save_path(request):
    if request.GET:
        user_id = request.GET.get('user_id')
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        name = request.GET.get('name')
        # t_time = request.GET.get('time')
        t_time = int(time.time())
        path = UserPath(lat=lat, lng=lng, name=name, time=t_time)
        try:
            path.save()
            return JsonResponse({'data': '存储路径成功', 'code': 1})
        except Exception as e:
            print(e)
            return JsonResponse({'data': '存储路径失败', 'code': 0})
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


def get_path(request):
    if request.GET:
        left_time = request.GET.get('left_time')
        right_time = request.GET.get('right_time')
        # t_time = 1597651766
        name = request.GET.get('name')
        # user_id = request.GET.get('user_id')
        LIMIT_DISTANCE = 0.001  # 在该范围内则视为被接触
        data = UserPath.objects.filter(
            time__lt=right_time, time__gt=left_time, name=name).values('lat', 'lng', 'time')
        # data = decode(data)
        print(data)
        contacted_peoples = {}
        for d in data:
            tp_ltime = d['time'] - 24 * 60 * 60 
            tp_rtime = d['time'] + 24 * 60 * 60  # tp_ltime,tp_rtime构成一个时间段，前后24小时
            print(unix_to_datetime(tp_ltime),unix_to_datetime(tp_rtime))
            lng = d['lng']
            lat = d['lat']
            # 查询一定时间范围内，可能接触到的人
            infos = UserPath.objects.filter(time__lt=tp_rtime, time__gt=tp_ltime, lng__lt=lng + LIMIT_DISTANCE,
                                           lng__gt=lng - LIMIT_DISTANCE, lat__lt=lat + LIMIT_DISTANCE, lat__gt=lat - LIMIT_DISTANCE).values()
            for info in infos:
                if info['name']==name: # 接触到的人之中不包括自己
                    continue
                contacted_peoples[info['name']] = info['time']
        # print('我是data',data)
        return JsonResponse({'data': list(data), 'code': 1, 'contacted_proples': contacted_peoples})
    else:
        return JsonResponse({'data': '请求方式错误,或未传输数据', 'code': 0})


def get_user_info_by_mail(request):
    if request.GET:
        mail = request.GET.get('mail')
        # id = '1'
        user = User.objects.filter(mail=mail).values(
            'name', 'school', 'authority', 'src', 'major', 'classes', 'academy', 'sex', 'identity_id', 'mail')
        # 返回格式
        # {user：[{}{}{}{}]}
        return JsonResponse({'data': list(user), 'code': 1})

def set_class_status(request):
    if request.GET:
        place = request.GET.get('place')
        state = request.GET.get('state')
        id = request.POST.get('user_id')
        user = User.objects.filter(pk=id).get()
        authority = user.authority
        try:
            temp_place = ClassroomNumber.objects.filter(place=place).get()
            # print('state',state==temp_place.state)
            if authority == '0':
                # print(temp_place.state)
                temp_place.state = state
                temp_place.save()
            elif temp_place.administrators == authority:
                # print(temp_place.state)
                temp_place.state = state
                temp_place.save()
            else:
                return JsonResponse({'data': '没有权限!', 'code': 0})
            return JsonResponse({'data': '成功', 'code': 1})
        except Exception as e:
            return JsonResponse({'data': '未知错误', 'code': 0})

def make_data_for_school_hospital(request):
    for _ in range(random.randint(0,10)):
        date = datetime.datetime.now()
        user = User.objects.filter(pk = 1).get()
        for i in range(31):
            temp = date
            tpDate = -i # 偏移日期量
            temp = date + datetime.timedelta(days=tpDate)
            temp = temp.strftime('%Y-%m-%d')
            symptom = ['有干咳症状','其它','其他','其他','其他','其他','其他']
            index = random.randint(0,6)
            place = SchoolHospitalAppointment(symptom = symptom[index], time = temp, state = 1, version = 0, user_id = user)
            place.save()
    return HttpResponse('ok')