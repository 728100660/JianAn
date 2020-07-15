from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, PlaceInfo, PlaceNumber, Notify, ClassRoom, SchoolHospitalAppointment,BuildInfo,ClassroomNumber,LatestNotify
import time,datetime
from .common import merge_dict_list

from django.db.models import Sum,Max
# Create your views here.


def test(request):
    # data = User.objects.filter(name='pxz').aggregate(Max('id'))
    # user_infor = User.objects.filter(name='pxz').values()
    # return JsonResponse({'user_info':list(user_infor)})
    # print(data)
    # data = User.objects.filter(name='pxz').get()
    # result = [data]
    # return JsonResponse(list(result),safe=False)
    return HttpResponse('asdf')


    # rooms = {'A1','B1','C1','D1','A2','B2','C2','D2','A3','B3','C3','D3'}
    # for room in rooms:
    #     for i in range(10):
    #         i+=1
    #         if i < 10:
    #             temp_room = room+'0'+str(i)
    #         else:
    #             temp_room = room+str(i)
    #         print(temp_room)
    #         place = ClassroomNumber(place=temp_room,real_time_number=i*5,max_people=i*10,state=1)
    #         place.save()
    # return HttpResponse('成功')

    places = ['校医院','贤德书院','萃雅书院','陌陌书院','贤德食堂','萃雅食堂','楚枫轩食堂','岭南咸嘉食堂','至诚楼','日新楼','乐知楼','博学楼','图书馆']
    for place in places:
        place = PlaceNumber(place=place,real_time_number=11,max_people=100,state=1,administrators=1)
        place.save()
    return HttpResponse('添加成功')

# 注册账户信息
def register(request):
    password = '123456'
    authority = '1'
    phone_number = '1234526721'
    student_number = '1234526712'
    name = 'pxz'
    academy = '计算机与信息工程学院'
    classes = '1'
    sex = '0'
    major = '物联'
    user = User(password=password, authority=authority,
                phone_number=phone_number, student_number=student_number, name=name, academy=academy, classes=classes, sex=sex, major=major)
    if User.objects.filter(phone_number=phone_number).exists():
        return HttpResponse('该手机号码已经注册过账户了')
    elif User.objects.filter(student_number=student_number).exists():
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
        student_number = request.POST.get('student_number')
        # phone_number = '12345672'
        # student_number = '12345672'
        if User.objects.filter(phone_number=phone_number).exists():
            # data = User.objects.filter(phone_number=phone_number).values()
            return JsonResponse({'data':'该微信账号已被注册','code':0})
        else:
            data = User.objects.filter(student_number=student_number).get()
            if data.phone_number:
                return JsonResponse({'data':'该学号已被绑定','code':0})
            else:
                data.phone_number = phone_number
                data.save()
                return JsonResponse({'data':'绑定成功','code':1})


# 登录
# def login(request):
#     phone_number = '12345678'
#     student_number = '1234567'
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
#     elif User.objects.filter(student_number=student_number).exists():
#         users = User.objects.filter(student_number=student_number)
#         for user in users:
#             if user.password == password:
#                 return HttpResponse('登录成功')
#             else:
#                 return HttpResponse('defeat')
#     else:
#         return HttpResponse('账号错误')


# 登录
def login(request):
    if request.POST:
        phone_number = request.POST.get('phone_number')
        school = request.POST.get('school')
        student_number = request.POST.get('student_number')
        # phone_number = '12345672'
        if User.objects.filter(phone_number=phone_number).exists():
            data = User.objects.filter(phone_number=phone_number).values()
            if data[0]['student_number']==student_number:
                return JsonResponse({'data':list(data),'code':1})
            else:
                return JsonResponse({'data':'手机号码与学号不一致','code':0})
        else:
            data = User.objects.filter(student_number=student_number).get()
            if data.phone_number:
                return JsonResponse({'data':'手机号码与学号不一致','code':0})
            else:
                data.phone_number = phone_number
                data.save()
            data = User.objects.filter(phone_number=phone_number).values()
            return JsonResponse({'data':list(data),'code':1})
            #     return JsonResponse({'data':data,'code':1})
            # return JsonResponse({'data':'请先绑定学生信息','code':0})


# 获取场所人数
def get_number(request):
    if request.GET:
        place = request.GET.get('place')
        flag = request.GET.get('flag')
        floor = request.GET.get('floor')
        # 如果有flag就将placenumber表中所有数据返回
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
                data = ClassroomNumber.objects.filter(place__contains=temp_index).values()
                result += data
            return JsonResponse({'data':result,'code':1})
        else:
            placenumber = PlaceNumber.objects.filter(place__contains=place).values()
        return JsonResponse({'data':list(placenumber),'code':1})
        

# 获取用户信息
# 后期完善 
# get请求方式id 
def get_user_info(request):
    if request.GET:
        id = request.GET.get('user_id')
        # id = '1'
        user = User.objects.filter(pk=id).values('name','school','authority','src','major','classes','academy')
        # 返回格式 
        # {user：[{}{}{}{}]}
        return JsonResponse({'data':list(user),'code':1})

# 修改个人信息
# 后期完善 
# change（忘记专业术语了）请求方式
def modify_information(request):
    return JsonResponse({'code':1})

# 发布通知
def sent_notify(request):
    if request.POST:
        title = request.POST.get('title')
        content = request.POST.get('content')
        id = request.POST.get('user_id')

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
        notify = Notify(title=title,publisher=user,release_time=release_time,content=content)
        try:
            notify.save()
        except Exception as e:
            print(e)
            return JsonResponse({'data':'发布通知失败!','code':0})
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
                return({'data':'发布通知成功，但是更新信息失败','code':1})
        else:
            notify = LatestNotify(title=title,publisher=user,release_time=release_time,content=content)
            try:
                notify.save()
            except Exception as e:
                print(e)
                return({'data':'发布通知成功，但是更新信息失败','code':1})
        return JsonResponse({'data':'发布通知成功!','code':1})

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
    return JsonResponse({'data':'未使用POST方式传值，或者未传输数据到后台','code':0})

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
            print(place)
            print(type(place),place)
            temp_place = PlaceNumber.objects.filter(place=place).get()
            # print('state',state==temp_place.state)
            if authority == '0':
                # print(temp_place.state)
                temp_place.state=state
                temp_place.save()
            elif temp_place.administrators == authority:
                # print(temp_place.state)
                temp_place.state=state
                temp_place.save()
            else:
                return JsonResponse({'data':'没有权限!','code':0})
            # try:
            #     temp_place = PlaceNumber.objects.filter(place=place).get()
            #     print(temp_place.state)
            #     temp_place.state=state
            #     temp_place.save()
            # except Exception as e:
            #     print(e)
            #     return JsonResponse({'code':0})
            return JsonResponse({'data':'成功','code':1})
        return JsonResponse({'data':'失败，未接收到place数据','code':0})
    return JsonResponse({'data':'失败，请求方式失败或未接受到任何传值，请用get方法传值','code':0})
    


# 医院预约功能
def appointment(request):
    if request.POST:
        user_id = request.POST.get('user_id')
        symptom = request.POST.get('symptom')
        state = request.POST.get('state')
        time = request.POST.get('time')
        # user_id = '1'
        # symptom = 'symptom'
        # state = '1'
        # time 是预约时间，不是当前时间
        # time = datetime.datetime.now()
        # 当前时间
        now_time = datetime.datetime.now()
        # user = User.objects.filter(pk=id).get()
        # 判断当前用户是否预约
        if SchoolHospitalAppointment.objects.filter(user_id=user_id,time__gt=now_time).exists():
            if state == '1':
            # 如果是预约请求的话
            # 您已经预约过一次了，请先取消预约
                return JsonResponse({'data':'你已经预约过一次了','code':0})
            elif state == '3':
                # 如果是取消预约请求的话
                # 取消预约，预约人数减一
                try:
                    # 取消预约
                    hospital = SchoolHospitalAppointment.objects.filter(user_id=user_id,time__gt=time).get()
                    hospital.state = '3'
                    hospital.save()
                    # 人数减一
                    number = PlaceNumber.objects.filter(place='校医院').get()
                    placenumber = PlaceNumber(real_time_number=number.real_time_number-1)
                    placenumber.save()
                except Exception as e:
                    print(e,1)
                    return JsonResponse({'code':0})
                return JsonResponse({'data':'取消预约成功！','code':0})
        else:
            # 没有预约的话就预约
            # 预约
            # 如果用户是以前就有预约信息在数据库，获取最大版本号且新建一条预约信息将版本呢号＋1
            if SchoolHospitalAppointment.objects.filter(user_id=user_id).exists():
                max_v = SchoolHospitalAppointment.objects.filter(user_id=user_id).aggregate(Max('version'))
                print(max_v)
                user = User.objects.filter(pk=user_id).get()
                max_version = int(max_v['version__max'])
                hospital = SchoolHospitalAppointment(user_id=user,symptom=symptom,state=state,time=now_time,version=str(max_version+1))
                hospital.save()
                # max_v['version__max'] = int(max_v['version__max'])+1
                # hospital = SchoolHospitalAppointment.objects.filter(version=max_v['version__max'],user_id=user_id).get()
                # hospital.version = str(int(hospital.version)+1)
                # hospital.save()
            else:
                # 如果有预约信息，将其版本号置为1
                user = User.objects.filter(pk=user_id).get()
                hospital = SchoolHospitalAppointment(user_id=user,symptom=symptom,state=state,time=now_time,version='1')
                print(1)
                hospital.save()
                print(2)
                # 人数加一
                number = PlaceNumber.objects.filter(place='校医院').get()
                print(number.real_time_number)
                print(type(number.real_time_number))
                number.real_time_number = str(number.real_time_number+1)
                number.save()
            # except Exception as e:
            #     print(e,2)  
            #     return JsonResponse({'code':0})
            return JsonResponse({'data':'预约成功！','code':1})
    return JsonResponse({'data':'请求方式错误,或未传输数据','code':0})


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
        if SchoolHospitalAppointment.objects.filter(user_id=user_id,time__gt=now_time).exists():
            max_v = SchoolHospitalAppointment.objects.filter(user_id=user_id).aggregate(Max('version'))
            user_appointment = SchoolHospitalAppointment.objects.filter(version=max_v['version__max'],user_id=user_id).get()
            # 更新信息，没必要将version+1
            # user_appointment.version = str(int(hospital.version)+1)
            user_appointment.state = state
            user_appointment.save()
            return JsonResponse({'data':'完成预约！','code':1})
        else:
            return JsonResponse({'data':'该用户没有预约信息，无法完成预约','code':0})
    return JsonResponse({'data':'请求方式错误','code':0})


# 获取指定用户的预约信息
def get_appointment_info(request):
    if request.GET:
        user_id = request.GET.get('user_id')
        now_time = datetime.datetime.now()
        # appointment_infos = SchoolHospitalAppointment.objects.filter(time__gt=now_time).values('symptom','user_id')
        # appointment_infos = SchoolHospitalAppointment.objects.filter(time__lt=now_time).values('symptom','user_id','state')
        appointment_infos = SchoolHospitalAppointment.objects.filter(user_id=user_id).values('symptom','user_id','state')
        # print(appointment_infos)
        data = []
        for appointment_info in appointment_infos:
            user = User.objects.filter(pk=appointment_info['user_id']).values('id','student_number','name')
            # print(user,appointment_info)
            # user是queryset，要转换成列表
            # 将两个[{}]合并成一个[{}]，并添加到返回列表中
            listmerge = list(user) + [appointment_info]
            print(listmerge)
            data += merge_dict_list(listmerge)
        return JsonResponse({'data':data,'code':1})
    else:
        return JsonResponse({'data':'请求方式错误,或未传输数据','code':0})


# 获取所有通知内容
def get_notify(request):
    if request.method == 'GET':
        data = []
        user_id = request.GET.get('user_id')

        notifys = Notify.objects.all().values()
        for notify in notifys:
            user = User.objects.filter(pk=notify['publisher_id']).values('id','student_number','name')
            listmerge = list(user) + [notify]
            data += merge_dict_list(listmerge)
        return JsonResponse({'data':data,'code':1})
    else:
        return JsonResponse({'data':'请求方式错误','code':0})


# 获取当前用户所管理的区域
def get_place(request):
    if request.GET:
        # user_id = request.GET.get('user_id')
        authority = request.GET.get('authority')
        if authority=='0':
            places = PlaceNumber.objects.all().values()
        else:
            places = PlaceNumber.objects.filter(administrators=authority).values('place')
        return JsonResponse({'data':list(places),'code':1})
    else:
        return JsonResponse({'data':'请求方式错误,或未传输数据','code':0})


# 获取教学楼信息ab=academybuild
def get_ab_info(request):
    if request.method == 'GET':
        places = BuildInfo.objects.all().values()
        return JsonResponse({'data':list(places),'code':1})
    else:
        return JsonResponse({'data':'请求方式错误','code':0})


# 获取最新通知信息
def get_latest_notify(request):
    if request.method == 'GET':
        latest_notify = LatestNotify.objects.all().values()
        user = User.objects.filter(administrators=authority).values('place')
        return JsonResponse({'data':list(latest_notify),'code':1})
    else:
        return JsonResponse({'data':'请求方式错误','code':0})
