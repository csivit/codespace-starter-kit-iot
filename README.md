![Starter Kit Banner](description.png)

# codespace-starter-kit-iot

This is an *example code* to that runs on a raspberry pi that sends the power on a pin when command is recieved via mqtt.
See the resources for understanding mqtt

To run this code,clone this repo on github.
and on ssh

```
pip install -r requirements.txt
python run.py
```
Now to publish commands to it, install any mqtt client on android and set-up the topic 'hello/codespace'

Now when you publish 'ON' or 'OFF' to this topic, the pi recieves it and turns the corresponding pin ON/OFF.

Resources
- How to get started with Raspberry pi http://www.imore.com/how-get-started-using-raspberry-pi
- Getting started with mqtt http://www.hivemq.com/blog/how-to-get-started-with-mqtt