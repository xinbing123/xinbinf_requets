import redis

SALE_C1_IS = [1,2,3,338,302,4,137,6,7,5,8]
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis_cli = redis.Redis(connection_pool=pool, decode_responses=True)
