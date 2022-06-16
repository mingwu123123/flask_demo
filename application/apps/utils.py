from kafka import KafkaProducer, KafkaConsumer
import json

host = '1.15.187.167'
port = 9092
topic = 'tess'


class Producer:
    def __init__(self, host, port, topic):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=[f'{host}:{port}'], api_version=(0, 10))

    def send(self, value):
        self.producer.send(self.topic, json.dumps(value).encode('utf-8')).add_callback(
            self.on_send_success).add_errback(
            self.on_send_error)
        self.producer.flush()
        print(value)

    # 定义一个发送成功的回调函数
    def on_send_success(self, record_metadata):
        print(record_metadata.topic, record_metadata.partition, record_metadata.offset)

    # 定义一个发送失败的回调函数
    def on_send_error(self, excp):
        print(excp)


producer = Producer(host, port, topic)

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[f'{host}:{port}'],
    auto_offset_reset='earliest',  # 从头消费
    group_id='test82e4'
)

# producer.send('asee')
# for i in consumer:
#     print(i.key, i.value)
# # while True:
# #     msg = consumer.poll(timeout_ms=1000000)  # 从kafka 拉去最新的所有消息
# #     print(msg)
