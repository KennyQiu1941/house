import requests
from housesspider import settings
import pymongo
'''这里是用来下载包含有户型以及面积信息的图片'''


con = pymongo.MongoClient(host=settings.DATABASE_IP, port=settings.MONGODB_PORT)
db = con['lianjia_ershouhouse']
coll_namelist = db.list_collection_names()


def reduct_houseid(dbid):
    '''吧mongodb每一个数据的_id还原成house_id'''
    return dbid[dbid.find('a') + 1:]


def get_allPicUrl():
    '''这是一个遍历房屋信息数据库并去除里面房屋户型图片的url的迭代器'''
    for each_coll_name in coll_namelist:
        coll = db[each_coll_name]
        for eachdb_data in coll.find():
            tmp_list = [reduct_houseid(eachdb_data['_id'])]
            for eachurl in eachdb_data["detail"][8]:
                if 'x-se' in eachurl:
                    tmp_list.append(eachurl)
            yield tmp_list, eachdb_data, coll


def downer(url, house_id):
    '''下载图片'''
    agent = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    count = 1
    for each_url in url:
        with open('/home/pic/{}a{}.jpg'.format(house_id, count), 'wb') as f:
            f.write(requests.get(url=each_url, headers=agent).content)
            count += 1


if __name__ == '__main__':
    '''下载有户型信息的图片用于识别实际使用面积'''
    for eachurldata in get_allPicUrl():
        house_id, url, dbdata, coll = eachurldata[0][0], eachurldata[0][1:], eachurldata[1], eachurldata[2]
        try:
            dbdata['downed']
        except KeyError:
            downer(url=url, house_id=house_id)
            db_id = dbdata['_id']
            coll.update_one({'_id': db_id}, {'$set': {'downed': True}})
