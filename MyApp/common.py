
import time,datetime,random
import numpy as np
import rsa
def merge_dict_list(listmerge):
    """ 
    将list中的多个dict合并为一个，便于前端数据调用
    将两个[{}]合并成一个[{}]，并返回
    """
    temp_dict = {}
    data = []
    #外层循环用于遍历list的每个dict，内层循环用于遍历dict的key-value
    #index为tuple型，不能做int使用
    print('listmerge',listmerge)
    for index in enumerate(listmerge):
        print(index)
        for key in listmerge[index[0]]:
            #将原来的key-value存入空dict
            temp_dict[key] = listmerge[index[0]][key]
    #将合并的dict插入list中，数据格式为：[{},{},{}]
    data.append(temp_dict)
    return data


def unix_to_datetime(unixTime):
    dataArray = datetime.datetime.fromtimestamp(unixTime)
    result = dataArray.strftime("%Y--%m--%d %H:%M:%S")
    return result


def make_stage_number_for_dict(place, capacity):
    tpStreamList = {} # 其实是dict的
    if '贤德书院' in place:
        real_number = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        print(capacity,real_number,place)
    elif '萃雅书院' in place:
        real_number = random.randint(int(capacity * 0.8),int(capacity * 0.9))
        print(capacity,real_number,place)
    elif '陌陌书院' in place:
        real_number = random.randint(int(capacity * 0.3),int(capacity * 0.5))
        print(capacity,real_number,place)
    else:
        real_number = random.randint(int(capacity * 0.3),int(capacity * 0.7))
    if "食堂" in place:
        gaoFengNumber = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        normalNumber = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['seven'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['nine'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['eleven'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['thirteen'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['fifteen'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['seventeen'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['nineteen'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['twenty_one'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['real_number'] = real_number
    else:
        tpStreamList['seven'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['nine'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['eleven'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['thirteen'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['fifteen'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['seventeen'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['nineteen'] = random.randint(int(capacity * 0.5),int(capacity * 0.7))
        tpStreamList['twenty_one'] = random.randint(int(capacity * 0.1),int(capacity * 0.3))
        tpStreamList['real_number'] = real_number
    return tpStreamList


def get_number_stage(stage):
    '''把单词转换为数字时间段'''
    if stage == 'seven':
        return 7
    if stage == 'nine':
        return 9
    if stage == 'eleven':
        return 11
    if stage == 'thirteen':
        return 13
    if stage == 'fifteen':
        return 15
    if stage == 'seventeen':
        return 17
    if stage == 'nineteen':
        return 19
    if stage == 'twenty_one':
        return 21


def tongtai_encrypt(data):
    emessage = 'data'.encode('utf-8')
    (public_key, private_key) = rsa.newkeys(255)
    private_key = str(private_key)
    crypto = rsa.encrypt(emessage, public_key)
    return (str(crypto),private_key)# 将加密后的数据和公匙以元组的形式返回

def make_room(rooms):
    res = []
    for room in rooms:
        for i in range(10):
            i += 1
            if i < 10:
                temp_room = room+'0'+str(i)
                res.append(temp_room)
            else:
                temp_room = room+str(i)
                res.append(temp_room)
    return res


def decode(datas):
    res = []
    for data in datas:
        lat = eval(data['lat'])
        lng = eval(data['lng'])
        private_key = data['publicKey']
        if not private_key:
            res.append(data)
            continue
        tp_res = dict()
        tp_res['lat'] = rsa.decrypt(lat, private_key)
        tp_res['lng'] = rsa.decrypt(lng, private_key)
        tp_res['time'] = data['time']
        res.append(tp_res)
    return res


# 同态加密算法
def generate_key(w,m,n):
    S = (np.random.rand(m,n) * w / (2 ** 16))# 可证明 max(S) < w
    return S# key，对称加密
def encrypt(x,S,m,n,w):
    assert len(x) == len(S)
    e = (np.random.rand(m))# 可证明 max(e) < w / 2
    c = np.linalg.inv(S).dot((w * x) + e)   
    return c
def decrypt(c,S,w):
    return (S.dot(c) / w).astype('float')