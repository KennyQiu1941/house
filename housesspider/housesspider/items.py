# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HousesspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 信息连接
    house_url = scrapy.Field()
    # 房屋标题
    house_title = scrapy.Field()
    # 小区名称
    community_name = scrapy.Field()
    # 所在区域名称
    area_name = scrapy.Field()
    # 也是链家id
    house_id = scrapy.Field()
    # 经纪人名
    broker_name = scrapy.Field()
    # 电话
    phone_num = scrapy.Field()
    # 总价
    total_price = scrapy.Field()
    # 单位价格
    unit_price = scrapy.Field()
    # 房屋基本信息
    houses_detailed = scrapy.Field()
    # 交易信息
    houses_detailed1 = scrapy.Field()
    # 房屋照片连接
    houses_pic_urls = scrapy.Field()
    # 交易状态
    trading_status = scrapy.Field()