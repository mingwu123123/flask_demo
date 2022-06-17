from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

class Producer:
    def __init__(self, host, port, topic):
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=[f'{host}:{port}'], api_version=(0, 10))

    def send(self, key, value): # key@value
        self.producer.send(self.topic, key=json.dumps(key).encode('utf-8'), value=json.dumps(value).encode('utf-8')).add_callback(self.on_send_success).add_errback(
            self.on_send_error)
        self.producer.flush()

    #定义一个发送成功的回调函数
    def on_send_success(self, record_metadata):
        # print(record_metadata.topic, record_metadata.partition, record_metadata.offset)
        pass

    #定义一个发送失败的回调函数
    def on_send_error(self, excp):
        print(f"send error:{excp}")
        # handle exception

#
# KAFKA_HOST = '1.15.187.167'
# KAFKA_PORT = 9092
# producer = Producer(KAFKA_HOST, KAFKA_PORT, 'car')
# producer.send('car',  {'a': 's'})


# host = '1.15.187.167'
# port = 9092
# topic = 'tess'
#
#
# producer = Producer(host, port, topic)
# producer.send('asee')

