# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis_bloomfilter.spiders import RedisSpider
from ..items import HousesspiderItem
import re
import sys
import json
import requests


def getpingjia(house_id):
    '''通过房屋id和评价页码获取经纪人对房屋评价'''
    agent = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    tmp_list = []
    for page in range(1, 999):
        baseurl = 'https://sh.lianjia.com/ershoufang/showcomment?&page={}&id={}'.format(page, house_id)
        content_str = requests.get(url=baseurl, headers=agent).content
        content_json = json.loads(content_str)
        if content_json['data']:
            tmp_list.append(content_json)
        else:
            break
    return tmp_list


def get_baseurl(url):
    '''通过正则获取请求url前半部分用来和页面获取的url拼接'''
    return re.findall(r'(https://\w+\.lianjia\.com)/ershoufang/', url)[0]


def list_to_str(l):
    '''吧列表转换成带空格隔开的字符串'''
    return str(l).replace('[', '').replace(']', '').replace(',', '')


class HousesSpider(RedisSpider):
    name = 'house_spider'
    # start_urls = 'https://www.lianjia.com/city/'
    redis_key = 'house_spider:start_urls'

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表

    # def parse(self, response):
    #     '''解析全国城市列表得到城市url'''
    #     print(1)
    #     for citys in response.xpath(r'//ul[@class="city_list_ul"]//li'):
    #         for city in citys.xpath(r'.//div[@class="city_list"]//ul//li'):
    #             city_url = city.xpath(r'./a/@href').extract()[0]
    #             yield scrapy.Request(url=city_url + 'ershoufang/', callback=self.parse_city)

    def parse(self, response):
        '''解析城市页面得到区url如果放开上面一个方便并修改starturl将全国获取信息'''
        print(1)
        baseurl = get_baseurl(response.url)
        for area in response.xpath(r'//div[@data-role="ershoufang"]/div//a'):
            area_url = area.xpath(r'./@href').extract()[0]
            yield scrapy.Request(url='{}{}'.format(baseurl, area_url), callback=self.parse_area, dont_filter=True)

    def parse_area(self, response):
        '''解析区页面得到小区域url是最终房屋出售列表'''
        print(2)
        baseurl = get_baseurl(response.url)
        for each_area in response.xpath(r'//div[@data-role="ershoufang"]/div[2]//a'):
            each_area_url = each_area.xpath(r'./@href').extract()[0]
            yield scrapy.Request(url='{}{}'.format(baseurl, each_area_url), callback=self.parse_houselistnum,
                                 dont_filter=True)

    def parse_houselistnum(self, response):
        '''获取小区页面并将每一个页码连接返回给parse_housepage'''
        url = response.url
        try:
            totalpage = \
                json.loads(response.xpath(r'//div[@class="page-box house-lst-page-box"]/@page-data').extract()[0])[
                    'totalPage']
        except IndexError as e:
            yield scrapy.Request(url=url, callback=self.parse_housepage, dont_filter=True)
        else:
            for page in range(1, totalpage + 1):
                listurl = '{}pg{}'.format(url, page)
                yield scrapy.Request(url=listurl, callback=self.parse_housepage, dont_filter=True)

    def parse_housepage(self, response):
        '''解析页面获取每一个房屋的url详细页返回给parse_house_detail'''
        print(4)
        for eachhousepage in response.xpath(r'//ul[@class="sellListContent"]//li'):
            # url = eachhousepage.xpath(r'./a/@href').extract()[0]
            # print(url)
            yield scrapy.Request(url=eachhousepage.xpath(r'./a/@href').extract()[0], callback=self.parse_house_detail,
                                 dont_filter=True)

    def parse_house_detail(self, response):
        '''分析详情页获取信息'''
        print(5)
        item = HousesspiderItem()
        # 房屋详细页url
        item['house_url'] = response.url
        print(response.url)
        '''房屋标题'''
        item['house_title'] = response.xpath(
            r'//div[@class="sellDetailHeader"]/div[@class="title-wrapper"]/div[@class="content"]/div[@class="title"]/h1/text()').extract()[
            0]
        content_ele = response.xpath(r'//div[@class="overview"]/div[@class="content"]/div[@class="aroundInfo"]')
        # 小区名ls
        # 地区名
        item['area_name'] = list_to_str(
            content_ele.xpath(r'./div[@class="areaName"]/span[@class="info"]//a/text()').extract())
        # 房屋id
        item['house_id'] = content_ele.xpath(r'./div[@class="houseRecord"]/span[@class="info"]/text()').extract()[0]
        broker_ele = response.xpath(r'//div[@class="brokerInfoText fr LOGVIEWDATA"]')
        try:
            # 经纪人名
            item['broker_name'] = broker_ele.xpath(r'./div[@class="brokerName"]/a/text()').extract()[0]
            # 联系方式
            item['phone_num'] = list_to_str(broker_ele.xpath(r'./div[@class="phone"]/text()').extract())
        except IndexError:
            # 无经纪人
            item['broker_name'] = 'None'
            item['phone_num'] = 0
        price_ele = response.xpath(r'//div[@class="overview"]/div[@class="content"]/div[@class="price "]')
        try:
            # 房屋总价格
            item['total_price'] = price_ele.xpath(r'./span[@class="total"]/text()').extract()[0]
            # 房屋单价
            item['unit_price'] = price_ele.xpath(
                r'./div[@class="text"]/div[@class="unitPrice"]/span[@class="unitPriceValue"]/text()').extract()[
                0]
            # 交易状态  1表示可交易状态
            item['trading_status'] = b'1'
        except IndexError as e:
            # 下架后单价 用来捕捉以前的房源
            item['total_price'] = \
                response.xpath(r'//div[@class="price isRemove"]/span[@class="total"]/text()').extract()[0]
            # 单价
            item['unit_price'] = response.xpath(
                r'//div[@class="price isRemove"]/div[@class="text"]/div[@class="unitPrice"]/span[@class="unitPriceValue"]/text()').extract()[
                0]
            # 表示交易状态下架
            item['trading_status'] = b''
        houses_detailed_ele = response.xpath(r'//div[@class="introContent"]//div[@class="content"]//li')
        # 房屋基本属性
        item['houses_detailed'] = [
            {i.xpath(r'./span[@class="label"]/text()').extract()[0]: i.xpath(r'./text()').extract()[0]} for i in
            houses_detailed_ele]
        # 房屋交易属性
        houses_detailed_ele1 = response.xpath(r'//div[@class="introContent"]//div[@class="content"]//li')
        item['houses_detailed1'] = [
            {i.xpath(r'./span[@class="label"]/text()').extract()[0]: i.xpath(r'./text()').extract()[0]} for i in
            houses_detailed_ele1]
        # 房屋照片
        item['houses_pic_urls'] = [i.xpath(r'./@data-src').extract()[0] for i in
                                   response.xpath(r'//ul[@class="smallpic"]//li')]
        yield item
