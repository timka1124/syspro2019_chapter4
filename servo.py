import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(deg):
    degrees=((1.9*deg)/180.0+1.44)/20.0*100.0
    servo.ChangeDutyCycle(degrees)
    return degrees

while 1:
    val=input()
    if -90 <= val <=90:
        setservo(val)
    else:
        print("owari")
        break

GPIO.cleanup()


    






