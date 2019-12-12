#!/usr/bin/env python
import pika
import json
import requests

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='deti-engsoft-08.ua.pt', 
                            port=5672,
                            virtual_host='/',
                            credentials=pika.PlainCredentials('tomas', 'tomas25')))
channel = connection.channel()
channel.queue_declare(queue='comm_channel')
API_URL = 'localhost:8080/logs'

def callback(ch, method, properties, body):
    message = json.loads(body)
    msg_id = message['MESSAGE_ID']
    timestamp = message['TIMESTAMP']
    content = message['CONTENT']
    print(f'  [x] Received message [{msg_id}] at [{timestamp}]: {content}')
    
    # curl -X POST localhost:8080/logs -H 'Content-type:application/json' -d 
    #   '{"date": "2019-12-12 12:20:48.933046", "sensorId": 1, "sensorType": "door", "value": 0, "houseId": 1}'
    
    # API CALL
    req = requests.post(url = API_URL, data = content) 
    response = req.text 
    print(f'Response: {response}') 

    
    # ! DOOR_SENSOR
    if content['sensorType'] == 'DOOR_SENSOR':
        pass
    # ! FLAME_SENSOR
    elif content['sensorType'] == 'FLAME_SENSOR':
        pass
    # ! GAS_SENSOR
    elif content['sensorType'] == 'GAS_SENSOR':
        pass
    # ! HUMPLANTS_SENSOR
    elif content['sensorType'] == 'HUMPLANTS_SENSOR':
        pass
    # ! LIGHT_SENSOR
    elif content['sensorType'] == 'LIGHT_SENSOR':
        pass
    # ! PIR_SENSOR
    elif content['sensorType'] == 'PIR_SENSOR':
        pass
    # ! RAIN_SENSOR
    elif content['sensorType'] == 'RAIN_SENSOR':
        pass
    # ! SOUND_SENSOR
    elif content['sensorType'] == 'SOUND_SENSOR':
        pass
    # ! TEMP_SENSOR
    elif content['sensorType'] == 'TEMP_SENSOR':
        pass
    # ! HUM_SENSOR
    elif content['sensorType'] == 'HUM_SENSOR':
        pass
    # ! KNOCK_SENSOR    
    elif content['sensorType'] == 'KNOCK_SENSOR':
        pass
    # ! ERROR
    else:
        print('ERROR')

channel.basic_consume(
    queue='comm_channel', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()