import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)



# The callback for when the client receives a connect from the server.
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	if(msg.payload=='ON'):
		print "LED on"
		GPIO.output(18,GPIO.HIGH)
	elif(msg.payload=='OFF'):
		print "LED off"
		GPIO.output(18,GPIO.LOW)



# Subscribe to a topic, if it anyone aka the client publishes on the topic, we will recieve that
client.subscribe(“hello/world”)


#Connect to server and set up callback function for on_connect and on_message
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#This is an open broker to try mqtt
client.connect("iot.eclipse.org",1883,60)

# Loop this code
client.loop_forever()
