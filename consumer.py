from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

host = '1.15.187.167'
port = 9092
topic = 'tess'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[f'{host}:{port}'],
    auto_offset_reset='earliest', # 从头消费
    group_id='test82e4'
)

for i in consumer:
    print(i.key, i.value)
# while True:
#     msg = consumer.poll(timeout_ms=1000000)  # 从kafka 拉去最新的所有消息
#     print(msg)
#
# #获取主题列表
# print(consumer.topics() )
# #获取当前消费者订阅的主题
# print(consumer.subscription() )
# #获取当前消费者topic、分区信息
# print(consumer.assignment() )
# #获取当前消费者可消费的偏移量
# print(consumer.beginning_offsets(consumer.assignment()))
# #重置偏移量，从第5个偏移量消费
# consumer.seek(TopicPartition(topic=topic, partition=0), 5)
# #获取当前主题的最新偏移量
# print(consumer.position(TopicPartition(topic=u'test', partition=0)))
#
# #消费多个主题
# consumer = KafkaConsumer(bootstrap_servers=brokerlist)
# consumer.subscribe(topics=['test','test0'])  #订阅要消费的主题
# for message in consumer:
#     print(message)