import time
from multiprocessing import Pool
import redis
from producer import Producer

REDIS_HOST = 'tengxunyun'
REDIS_PORT = 6379
pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, db=2)   # 前端传入的数据放在db=2
redis_client = redis.Redis(connection_pool=pool)


KAFKA_HOST = 'tengxunyun'
KAFKA_PORT = 9092
# topic = 'tess'


data_types = ['car', 'singal']
def worker(data_type):
    producer = Producer(KAFKA_HOST, KAFKA_PORT, data_type) # 不同的
    calc_key = int(time.time()) - 100  # 向前计算100s
    while True:
        timestamp = int(time.time())
        if calc_key < timestamp - 5:  # 只计算当前时间 5s 前的数据
            keys = sorted(redis_client.keys(f'{data_type}-{calc_key}*'))
            for key in keys:
                value = redis_client.getdel(key)
                print(data_type, value)
                producer.send(data_type, value) # 同一个key=data_type 会被放置在同一分区，保证顺序
                # TODO 已排序，通过生产者发送至kafka，采用不同的 topic
            calc_key += 1  #计算下一秒的数据
        else:
            time.sleep(1)
            pass # 继续循环


if __name__ == "__main__":
    pool = Pool(len(data_types))  # 定义一个进程池，最大进程数3

    for i in data_types:
        pool.apply_async(worker, [i, ])  # 使用非阻塞方式调用func（并行执行，堵塞方式必须
        # 等待上一个进程退出才能执行下一个进程）

    pool.close()  # 关闭进程池，关闭后pool不能再添加新的请求
    pool.join()  # 等待pool中所有子进程执行完成，必须放在close语句之后
