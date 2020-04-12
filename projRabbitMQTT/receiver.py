#!/usr/bin/env python
import pika
import json
import requests

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='deti-engsoft-08.ua.pt', 
                            port=5672,
                            virtual_host='/',
                            credentials=pika.PlainCredentials()))
channel = connection.channel()
channel.queue_declare(queue='comm_channel')
API_URL = 'http://localhost:8080/logs'

def callback(ch, method, properties, body):
    message = json.loads(body)
    msg_id = message['MESSAGE_ID']
    timestamp = message['TIMESTAMP']
    content = message['CONTENT']
    print(f'  [x] Received message [{msg_id}] at [{timestamp}]: {content}')
    print(content, type(content))
    # API CALL
    req = requests.post(url = API_URL, data=content, headers = {'content-type': 'application/json'})
    response = req.text 
    print(f'Response: {response}') 


channel.basic_consume(
    queue='comm_channel', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
try:
    channel.start_consuming()
except Exception as e:
    print("error", e)
