# Import libraries

#Numbers 2 = 0°, 12 = 180°
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2

print("Wave maker starting")

# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)  
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Wait for 2 seconds
time.sleep(2)

servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

# Wait again for 2 seconds! :)
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)

# Another little 2 second pause...
time.sleep(2)

servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)
time.sleep(2)
servo2.ChangeDutyCycle(12)
servo1.ChangeDutyCycle(12)
time.sleep(2)
servo2.ChangeDutyCycle(7)
servo1.ChangeDutyCycle(7)


time.sleep(2)

#Clean things up at the end
servo1.stop()
servo2.stop()
GPIO.cleanup()
print ("Goodbye")
