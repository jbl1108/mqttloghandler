from logging import Handler
from logging import Formatter
from paho.mqtt import client

TOPIC = "measurements/syslog"


class MQTTLogHandler(Handler):

    def __init__(self, mqtt_client: client, method: str, silent: bool = True):
        super().__init__()
        self.client = mqtt_client
        self.setFormatter(Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", '
                                    '"tags": {"level": "%(levelname)s"}}'))
        self.silent = silent

    def emit(self, log_record):
        msg = self.format(log_record)
        self.client.publish(TOPIC, msg)
        if not self.silent:
            print(msg)



