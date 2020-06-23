from pykafka import KafkaClient
import json
from datetime import datetime
import uuid

# Create Producer
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['testBusdata']
producer = topic.get_sync_producer()

#Construct message
data = {}


def get_coordinates(path):
#Read Co-ordinates from Geo json
    json_array= json.load(open('./data/'+path))
    data['busline']='0000'+ path[-1]
    coordinates = json_array['features'][0]['geometry']['coordinates']
    #print(coordinates)
    return coordinates


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
        i+=1

generate_checkpoint(get_coordinates('route1'))
generate_checkpoint(get_coordinates('route2'))
generate_checkpoint(get_coordinates('route3'))