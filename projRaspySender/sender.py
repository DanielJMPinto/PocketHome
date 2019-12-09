#!/usr/bin/env python
import pika
import datetime
import uuid
import json

class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='working_queues', exchange_type='fanout')

    def send(self, message):
        message = {
            'MESSAGE_ID': str(uuid.uuid4()),
            'TIMESTAMP': str(datetime.datetime.now()),
            'CONTENT': message
        }
        self.channel.basic_publish(exchange='working_queues', routing_key='', body=json.dumps(message))
        print(f" [x] Sent {message}!")

sender = Sender()
while True:
    msg = input('Message: ')
    # Se nao inserir nada, desliga a conexão
    if not msg:
        sender.send('FINISHED_CONN')
        print('bye')
        sender.connection.close()
        break
    sender.send(msg)


