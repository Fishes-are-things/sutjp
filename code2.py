# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

try:
    while True:
        #Ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 & 180: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        servo2.ChangeDutyCycle(2+(angle/18))
        time.sleep(0)
        servo1.ChangeDutyCycle(0)
        servo2.ChangeDutyCycle(0)

finally:
    #Clean things up at the end
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
    print("Goodbye!")
