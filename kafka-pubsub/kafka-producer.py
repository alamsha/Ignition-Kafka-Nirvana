from kafka import KafkaProducer
import time
import urllib.request
import requests
import json

################

broker_address= "192.168.1.102"
port = 1883

timestamp = int(time.time())

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer



url = "http://192.168.1.102/smarttablechart/ignition_group1.php"
#url = "http://services.groupkt.com/state/get/IND/all"

response = requests.get(url)
data = response.json()
print ("url connected1...")
KAFKA_MSG=json.dumps(data);
#########

producer = connect_kafka_producer()
 
try:
    while True:
        time.sleep(4)
#        value = input('Enter to continue:')
        publish_message(producer, 'Area1-Zone1', 'parsed', KAFKA_MSG)

        url = "http://192.168.1.102/smarttablechart/ignition_group1.php"

        response = requests.get(url)
        data = response.json()
#        print ("url connected1...")
        KAFKA_MSG=json.dumps(data);

except KeyboardInterrupt:
    producer.close()


