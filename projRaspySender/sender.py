'''
Created Date: Thursday, November 14th 2019, 11:50:36 am
Author: tomas

Copyright (c) 2019 Tomás
'''
import pika
import json
import uuid

class RPCCli(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, text):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='comm_channel',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(text))
        while self.response is None:
            self.connection.process_data_events()
        return self.response


rpc_cli = RPCCli()
while True:
    response = rpc_cli.call('30')
    print(json.load(response))