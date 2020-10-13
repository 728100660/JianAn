
import time,datetime

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