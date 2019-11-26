import redis
from housesspider.settings import REDIS_HOST,REDIS_PORT
import time
'''定时发送start_url让scrapy进行增量采集'''

while True:
    rdb = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
    # 全国爬虫starturl
    # rdb.lpush('house_spider:start_urls','https://www.lianjia.com/city/')
    #上海爬虫starturl
    rdb.lpush('house_spider:start_urls','https://sh.lianjia.com/ershoufang/')
    print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    time.sleep(86400)

