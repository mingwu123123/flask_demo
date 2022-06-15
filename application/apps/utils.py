from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

class KafkaSend:
    def __init__(self, host, port):
        self.producer = KafkaProducer(
            # bootstrap_servers=[f'150.158.185.85:9092'],
            bootstrap_servers=[f'{host}:{port}'],
            key_serializer=lambda k: json.dumps(k).encode(),
            value_serializer=lambda v: json.dumps(v).encode())

        self.consumer = KafkaConsumer(
            'tess',
            bootstrap_servers=[f'{host}:{port}'],
            auto_offset_reset='earliest', # 从头消费
            group_id='test6'
        )

    def send(self, key, value, topic='tess'):
        self.producer.send(
            topic,
            key=key,
            value=value,
        )
        self.producer.flush()
        print(key, value)
        # try:
        #     future.get(timeout=10) # 监控是否发送成功
        # except kafka_errors:  # 发送失败抛出kafka_errors
        #     traceback.format_exc()


def consumer_demo():
    consumer = KafkaConsumer(
        'sun',
        bootstrap_servers=':9092',
        group_id='test'
    )
    for message in consumer:
        print("receive, key: {}, value: {}".format(
            json.loads(message.key.decode()),
            json.loads(message.value.decode())
            )
        )

def producer_demo():
    producer = KafkaProducer(
        bootstrap_servers=['150.158.185.85:9092'],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode())
    # 发送三条消息
    for i in range(0, 3):
        future = producer.send(
            'tess',
            key='count_num',  # 同一个key值，会被送至同一个分区
            value=str(i),
            )  # 向分区1发送消息
        print("send {}".format(str(i)))
        try:
            future.get(timeout=10) # 监控是否发送成功
        except kafka_errors:  # 发送失败抛出kafka_errors
            traceback.format_exc()

# producer_demo()
# # consumer_demo()
#
kafka_obj = KafkaSend('150.158.185.85', '9092')

kafka_obj.send('a', '5')
kafka_obj.send('b', '9')
print(333)

for i in kafka_obj.consumer:
    print(i.key, i.value)
