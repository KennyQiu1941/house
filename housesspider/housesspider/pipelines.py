# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from housesspider.settings import DATABASE_IP, MONGODB_PORT
import pymongo
import re
import time
from scrapy import logformatter


def get_city(response_url):
    return re.findall(r'https://(\w+).lianjia.com/ershoufang/\d+.html', response_url)[0]


def format_id(house_id):
    '''将房屋id格式化为mongodb接受的_id'''
    return '{}a{}'.format((23 - len(house_id)) * '0', house_id)


class HousesspiderPipeline(object):
    def __init__(self):
        con = pymongo.MongoClient(host=DATABASE_IP, port=MONGODB_PORT)
        self.db = con['lianjia_ershouhouse']

    def process_item(self, item, spider):
        '''将获取的数据写入mongodb后续加入其他组件例如新增数据经过筛选发送邮件
           数据格式分为三个字典，detail里是一个房屋信息的列表，由于价格信息可能更新并需要记录更新的历史所以不在这个列表里单独列为一个字典'''
        now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        house_url = item['house_url']
        coll = self.db[get_city(house_url)]
        house_id = item['house_id']
        total_price = item['total_price']
        unit_price = item['unit_price']
        mongo_house_id = format_id(house_id)
        house_data = coll.find_one({'_id': mongo_house_id})
        if house_data:
            if house_data['total_price'][-1][0] != total_price:
                coll.update_one({'_id': mongo_house_id},
                                 {'$push': {'total_price': [total_price, now_time], 'unit_price': unit_price}})
                print('{}-->{}'.format(house_data['total_price'][-1][0], total_price))
            else:
                print('数据未改变')
        else:
            coll.insert({'_id': mongo_house_id,
                         'detail': [house_url, item['house_title'], item['community_name'], item['area_name'],
                                    item['broker_name'], item['phone_num'], item['houses_detailed'],
                                    item['houses_detailed1'], item['houses_pic_urls'], item['trading_status']],
                         'total_price': [[item['total_price'],now_time]],
                         'unit_price': [item['unit_price']]})
            print('插入新数据')
            return item
