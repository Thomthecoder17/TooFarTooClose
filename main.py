import time
import board
import digitalio
import adafruit_hcsr04
import espnow
import random

# ESP Now setup
# e = espnow.ESPNow()
# peer = espnow.Peer(mac=b'0xe4\0xb0\0x63\0x84\0xcf\0x9c')
# e.peers.append(peer)

#Define the sensor with the correct pins
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO2, echo_pin=board.IO1)

rLed = digitalio.DigitalInOut(board.IO40)
gLed = digitalio.DigitalInOut(board.IO41)
rLed.direction = digitalio.Direction.OUTPUT
gLed.direction = digitalio.Direction.OUTPUT

far = True

while far:
    requiredDist = random.randint(50, 200)
    try:
        distance = sonar.distance
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)
        if distance < requiredDist:
            far = False
            # e.send(-1)
            gLed.value = False
            rLed.value = True
        elif distance > requiredDist:
            # e.send(1)
            gLed.value = False
            rLed.value = False
        elif distance == requiredDist:
            # e.send(0)
            gLed.value = True
            rLed.value = False
    except RuntimeError:
        print("Retrying... Sensor error")
    time.sleep(0.5)
    
    

