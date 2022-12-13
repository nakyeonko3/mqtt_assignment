import paho.mqtt.client as mqtt
import time

from datetime import datetime
from make_csv_file import make_csvfile

topic = "outTopic"
host = 'nakyeonkopi.local'
client_name = "flaskMainPy"

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)

def on_message(client, userdata, msg):
    make_csvfile(msg.payload.decode("utf-8"))

def mqtt_init():
    client = mqtt.Client(client_name)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host) #접속할 호스트명
    client.loop_start()


if __name__ == "__main__":
    mqtt_init()
    while True:
        time.sleep(1)