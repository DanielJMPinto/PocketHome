#!/usr/bin/env python
import pika
import datetime
import uuid
import json

class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.1.94"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='comm_channel')

    def send(self, message):
        message = {
            'MESSAGE_ID': str(uuid.uuid4()),
            'TIMESTAMP': str(datetime.datetime.now()),
            'CONTENT': message
        }
        self.channel.basic_publish(exchange='', routing_key='comm_channel', body=json.dumps(message))
        print(f" [x] Sent {message}!")

sender = Sender()
while True:
    msg = input('Message: ')
    if not msg:
        sender.send('FINISHED_CONN')
        print('bye')
        sender.connection.close()
        break
    sender.send(msg)

