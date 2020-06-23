import time
from pykafka import KafkaClient
import json
from datetime import datetime
import uuid

# Create Producer
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['geodata_final']
producer = topic.get_sync_producer()

#Construct message
data = {}
data['busline']='00001'

#Read Co-ordinates from Geo json
json_array= json.load(open('./data/route1'))
coordinates = json_array['features'][0]['geometry']['coordinates']
#print(coordinates)

def generate_uuid():
    return uuid.uuid4()

def generate_checkpoint(coordinates):
    i= 0
    while i < len(coordinates):
        data['key']= data['busline']+'_'+str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude']= coordinates[i][1]
        data['longitude']= coordinates[i][0]
        message= json.dumps(data)
        print(message)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        #if bus reaches last coordinate, restart
        if i == len(coordinates)-1:
            i=0
        else:
            i += 1


generate_checkpoint(coordinates)