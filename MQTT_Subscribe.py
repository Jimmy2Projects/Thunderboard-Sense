import time
import paho.mqtt.client as paho

broker="test.mosquitto.org"
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port, keepalive=60, bind_address="")                                 #establish connection

while True:

    print("================================================")

    print("Subscribing to topic","Thunderboard/Temperature\n>>>")
    client1.subscribe("Thunderboard/Temperature")

    print("Subscribing to topic","Thunderboard/Humidity\n>>>")
    client1.subscribe("Thunderboard/Humidity")

    print("Subscribing to topic","Thunderboard/Magnetic\n>>>")
    client1.subscribe("Thunderboard/Magnetic")

    print("Subscribing to topic","Thunderboard/Light\n>>>")
    client1.subscribe("Thunderboard/Light")

    print("Subscribing to topic","Thunderboard/UV\n>>>")
    client1.subscribe("Thunderboard/UV")
    print("================================================\n\n\n")

    time.sleep(1)
