import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "sensor1"
AIO_USERNAME = "macundkase"
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    client.publish("sensor1", random.randint(20, 70))
    client.publish("sensor2", random.randint(0, 100))
    client.publish("sensor3", random.randint(0, 100))
