'''
Created Date: Thursday, November 14th 2019, 11:50:44 am
Author: tomas

Copyright (c) 2019 Tomás
'''
# This receiver will be implemented in java, this is just a tester

import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='comm_channel')

def on_request(ch, method, props, body):
    msg = json.loads(body)
    print(msg)
    # 
    # if msg['upd_values']:
        # response = 'received'

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body='teste')

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='comm_channel', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
