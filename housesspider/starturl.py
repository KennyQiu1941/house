import redis
from housesspider.settings import REDIS_HOST,REDIS_PORT
import time




while True:
    rdb = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
    # '''全国爬虫starturl'''
    # rdb.lpush('house_spider:start_urls','https://www.lianjia.com/city/')
    '''上海爬虫starturl'''
    rdb.lpush('house_spider:start_urls','https://sh.lianjia.com/ershoufang/')
    time.sleep(86400)

