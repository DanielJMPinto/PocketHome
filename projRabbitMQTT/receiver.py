#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='working_queues', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='working_queues', queue=queue_name)

def callback(ch, method, properties, body):
    print(body)
    message = json.loads(body)
    msg_id = message['MESSAGE_ID']
    timestamp = message['TIMESTAMP']
    content = message['CONTENT']
    print(f'  [x] Received message [{msg_id}] at [{timestamp}]: {content}')


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()