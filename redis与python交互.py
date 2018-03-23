from redis.client import StrictRedis

if __name__ == '__main__':
    strict_redis = StrictRedis(host='127.0.0.1',port=6379,db=0,decode_responses=True)

    strict_redis.set('aa','111')
    strict_redis.set('bb','222')
    strict_redis.set('cc','333')

    aa = strict_redis.get('aa')
    bb = strict_redis.get('bb')
    cc = strict_redis.get('cc')
    dd = strict_redis.get('dd')

    print(aa,bb,cc)

    keys = strict_redis.keys()
    print(keys,type(keys))