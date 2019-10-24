'''数据类型占用空间测试'''
# import sys
#
#
#
# a = b'3333333333'
# aa = 3333333333
# aaa = '3333333333'
#
# b = 'nihao'
# bb = b'nihao'
#
# c = '你好'
# cc = bb.decode('utf8')
#
# def getsize(*args):
#     for i in args:
#         print('类型：{}，占用空间： {}'.format(type(i), sys.getsizeof(i)))
#
#
# getsize(c,cc)
# getsize(b,bb)


# '''测试房屋评价'''
# import requests
# import json
# def getpingjia(house_id):
#     '''通过房屋id和评价页码获取经纪人对房屋评价'''
#     agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
#     tmp_list = []
#     for page in range(1,999):
#         baseurl = 'https://sh.lianjia.com/ershoufang/showcomment?&page={}&id={}'.format(page,house_id)
#         content_str = requests.get(url=baseurl, headers=agent).content
#         content_json = json.loads(content_str)
#         if content_json['data']:
#             tmp_list.append(content_json)
#         else:
#             break
#     return tmp_list
#
# count = 0
# for i in getpingjia(107101123014):
#     print(i['data'])
#     count+=2
# print(count)


# '''模拟获取房价'''
# import requests
# from lxml import etree
# agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
# def text():
#     url = 'https://sh.lianjia.com/ershoufang/107100439681.html'
#     html = etree.HTML(requests.get(url=url,headers=agent).content.decode('utf8'))
#     return html.xpath(r'//div[@class="overview"]/div[@class="content"]/div[@class="price "]//span[@class="unit"]/span/text()')[0]
#
# print(text())
from housesspider.settings import DATABASE_IP, MONGODB_PORT
import pymongo

data = {
    "_id" : "000000000000a47066586585",
    "price" : [
        [
            "42.00",
            "20190908141122"
        ],
        [
            "-1.00",
            "20190911072559"
        ],
        [

            "42.00",
            "20190927055310"
        ]
    ]
}

data ={
    "_id" : "00000000000a107000678533",
    "detail" : [
        "https://sh.lianjia.com/ershoufang/107000678533.html",
        "鸿宝一村 2003年现浇房 满五年唯一 复式房",
        "鸿宝一村(南区)",
        "'奉贤' '西渡'",
        "彭少梅",
        "'4008650856' '0035'",
        [
            {
                "房屋户型" : "4室2厅1厨2卫"
            },
            {
                "所在楼层" : "高楼层 (共6层)"
            },
            {
                "建筑面积" : "162㎡"
            },
            {
                "户型结构" : "复式"
            },
            {
                "套内面积" : "暂无数据"
            },
            {
                "建筑类型" : "板楼"
            },
            {
                "房屋朝向" : "南"
            },
            {
                "建筑结构" : "砖混结构"
            },
            {
                "装修情况" : "毛坯"
            },
            {
                "梯户比例" : "一梯四户"
            },
            {
                "配备电梯" : "无"
            },
            {
                "产权年限" : "70年"
            },
            {
                "挂牌时间" : "\n                              "
            },
            {
                "交易权属" : "\n                              "
            },
            {
                "上次交易" : "\n                              "
            },
            {
                "房屋用途" : "\n                              "
            },
            {
                "房屋年限" : "\n                              "
            },
            {
                "产权所属" : "\n                              "
            },
            {
                "抵押信息" : "\n                              "
            },
            {
                "房本备件" : "\n                              "
            }
        ],
        [
            {
                "房屋户型" : "4室2厅1厨2卫"
            },
            {
                "所在楼层" : "高楼层 (共6层)"
            },
            {
                "建筑面积" : "162㎡"
            },
            {
                "户型结构" : "复式"
            },
            {
                "套内面积" : "暂无数据"
            },
            {
                "建筑类型" : "板楼"
            },
            {
                "房屋朝向" : "南"
            },
            {
                "建筑结构" : "砖混结构"
            },
            {
                "装修情况" : "毛坯"
            },
            {
                "梯户比例" : "一梯四户"
            },
            {
                "配备电梯" : "无"
            },
            {
                "产权年限" : "70年"
            },
            {
                "挂牌时间" : "\n                              "
            },
            {
                "交易权属" : "\n                              "
            },
            {
                "上次交易" : "\n                              "
            },
            {
                "房屋用途" : "\n                              "
            },
            {
                "房屋年限" : "\n                              "
            },
            {
                "产权所属" : "\n                              "
            },
            {
                "抵押信息" : "\n                              "
            },
            {
                "房本备件" : "\n                              "
            }
        ],
        [
            "https://vrlab-image.ljcdn.com/release/auto3dhd/7487d151bf0c01771cfc974c6233fdf0/screenshot/1555572617_1/pc0_nWnKpGcEn.jpg.q_70.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-b084055c-9350-4f39-9f6a-41c17293b253.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-bc9c93fe-65b3-4ebf-82a7-2424593b8b3f.jpg.710x400.jpg",
            "https://image1.ljcdn.com/x-se/hdic-frame/prod-6bf89c22-f762-4ba8-80b1-55145983c344.png.533x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-42e9b3f8-aef1-4c1c-a8fd-f596c9662a9d.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-a7211af8-6e9e-451d-88e3-58202a9b0c98.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-1604857b-11f5-4b1c-b8da-b587d14255d5.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-08846f54-4b3d-49a3-9ddd-abd789041a3d.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-38e6067d-3b56-44b3-87af-9ea524dafd72.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-97d050e3-306d-4d7f-9107-b6dcfc6904f6.jpg.710x400.jpg",
            "https://image1.ljcdn.com/310000-inspection/prod-de4f1aeb-1cf0-4008-adca-181e64afceac.jpg.710x400.jpg"
        ],
        b'1'
    ],
    "total_price" : [
        [
            "265",
            "20191023043159"
        ]
    ],
    "unit_price" : [
        "16359"
    ]
}
import time
from down_pic import reduct_houseid
def format_id(house_id):
    '''将房屋id格式化为mongodb接受的_id'''
    return '{}a{}'.format((23 - len(house_id)) * '0', house_id)

class HousesspiderPipeline(object):
    def __init__(self):
        con = pymongo.MongoClient(host=DATABASE_IP, port=MONGODB_PORT)
        self.db = con['lianjia_ershouhouse_test']

    def inter(self):
        coll = self.db['sh']
        data = coll.find_one({'_id':'00000000000a107000678533'})
        a = data['ddd']
        # coll.update_one({'_id':'00000000000a107000678533'},{'$set':{'downed':True}})
        # coll.insert(data)
        # # coll.update_one({'_id':format_id('107000678533')},{'$push':{'total_price':[333,2232],'unit_price':393939}})
        # for i in coll.find():
        #     picelist = [reduct_houseid(i['_id'])]
        #     for eachpic in i["detail"][8]:
        #         if 'x-se' in eachpic:
        #             picelist.append(eachpic)
        #     if len(picelist) >= 3:
        #         print(picelist)
#
h = HousesspiderPipeline()
d = h.inter()
# import re
#
# def get_city(response_url):
#     return re.findall(r'https://(\w+).lianjia.com/ershoufang/\d+.html',response_url)[0]
#
#
# print(get_city('https://sh.lianjia.com/xiaoqu/5011000004510/'))

# a = [
#             "https://vrlab-image.ljcdn.com/release/auto3dhd/7487d151bf0c01771cfc974c6233fdf0/screenshot/1555572617_1/pc0_nWnKpGcEn.jpg.q_70.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-b084055c-9350-4f39-9f6a-41c17293b253.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-bc9c93fe-65b3-4ebf-82a7-2424593b8b3f.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/x-se/hdic-frame/prod-6bf89c22-f762-4ba8-80b1-55145983c344.png.533x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-42e9b3f8-aef1-4c1c-a8fd-f596c9662a9d.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-a7211af8-6e9e-451d-88e3-58202a9b0c98.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-1604857b-11f5-4b1c-b8da-b587d14255d5.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-08846f54-4b3d-49a3-9ddd-abd789041a3d.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-38e6067d-3b56-44b3-87af-9ea524dafd72.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-97d050e3-306d-4d7f-9107-b6dcfc6904f6.jpg.710x400.jpg",
#             "https://image1.ljcdn.com/310000-inspection/prod-de4f1aeb-1cf0-4008-adca-181e64afceac.jpg.710x400.jpg"
#         ]
#
# for i in a:
#     if 'x-se' in i:
#         print(i)

# pic_list = ['https://image1.ljcdn.com/x-se/hdic-frame/79779058-9268-4986-811e-bce25c0ad7a7.png.533x400.jpg', 'https://image1.ljcdn.com/x-se/hdic-frame/0e416b37-7004-4ee8-9f6e-6fe41ef0c8ed.png.533x400.jpg', 'https://image1.ljcdn.com/x-se/hdic-frame/72c5e860-4736-433a-8324-f8771d36f3d2.png.533x400.jpg', 'https://image1.ljcdn.com/x-se/hdic-frame/2a612e20-e899-4265-87e3-e511bf92b39a.png.533x400.jpg', 'https://image1.ljcdn.com/x-se/hdic-frame/c92b7388-6aa7-4bcf-a650-41378864e2b8.png.533x400.jpg']
#
# from down_pic import downer
#
#
# downer(url=pic_list,house_id=['107100072279'])