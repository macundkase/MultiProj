import random
import time
import sys
from Adafruit_IO import MQTTClient
import requests

AIO_FEED_ID = "Equation"
AIO_USERNAME = "macundkase"
AIO_KEY = ""

global_equation = "x1 + x2 + x3"

def init_global_equation():
    headers = ()
    aio_url = "https://io.adafruit.com/api/v2/macundkase/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data=x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)

def modify_value(x1, x2, x3):
    global global_equation
    print("Equation: ", global_equation)
    result = eval(global_equation)
    print(result)
    return(result)

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
    if (feed_id == "equation"):
        global_equation = payload
        print(global_equation)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
init_global_equation()

while True:
    time.sleep(5)
    x1 = random.randint(20, 70)
    x2 = random.randint(0, 100)
    x3 = random.randint(0, 14)
    # client.publish("sensor1", x1)
    # client.publish("sensor2", x2)
    # client.publish("sensor3", x3)
    x4 = modify_value(x1, x2, x3)
    print(x4)
    pass