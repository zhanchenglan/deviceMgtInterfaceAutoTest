"""

@author:F2849440

@Description:描述

@file:mqtt.py

@time:2021/09/22

"""
import datetime
import json
import time

from paho.mqtt.client import Client

from src.main.common.logging import log


class mqttUtil:
    __attr__ = [
        "user_name",
        "pass_word",
        "host",
        "port",
        "client_id"
        "qos"
    ]

    def __init__(self, host=None, port=1883,
                 user_name=None, pass_word=None, client_id="mqttx_4f37ebf4", qos=0):
        self.user_name = user_name
        self.pass_word = pass_word
        self.host = host
        self.port = port
        self.client_id = client_id
        self.qos = qos

    def connect_mqtt(self):
        mqtt_client = Client()
        mqtt_client.username_pw_set(self.user_name, self.pass_word)
        res = mqtt_client.connect(host=self.host, port=self.port)
        if res == 0:
            log.info("Connected to MQTT Broker!")
        else:
            log.info("Failed to connect, return code %s", res)

        return mqtt_client

    def publish(self, payload, topic):
        payload = json.dumps(payload, ensure_ascii=False)
        cli = self.connect_mqtt()
        result = cli.publish(topic, payload, self.qos)
        cli.loop_start()
        status = result[0]
        if status == 0:
            log.info("Send %s msg %s", topic, payload)
        else:
            log.info("Failed to send message to topic %s", topic)

    def subscribe(self, topic):
        def on_message(client, userdata, msg):
            print(msg.topic + " message" + ":" + str(msg.payload))
            log.info("Received %s from %s topic", msg.payload.decode(), msg.topic)

        cli = self.connect_mqtt()
        cli.subscribe(topic, self.qos)
        cli.on_message = on_message
        cli.loop_forever()


if __name__ == "__main__":
    topic = "fromDevice/devices/zhantest1122/me/ruleTab/deviceInfo"
    payload = {
        "devId": "12qw",
        "vin": "1234568",
        "color": "白色",
        "type": "吉利帝豪s",
        "uploadTime": "2021-08-26 10:00:00"
    }

    # host = 'pre.mqtt.mobiledrive.ai'
    # port = 1883
    host = "121.41.109.132"
    port = 1833

    user_name = "zhantest1122"
    pass_word = "zhantest1122"

    mqtt = mqttUtil(host, port, user_name, pass_word)
    mqtt.publish(payload, topic)

    #mqtt.subscribe(topic)
