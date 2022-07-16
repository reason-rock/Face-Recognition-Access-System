import Jetson.GPIO as GPIO
import time

SERVO_PIN = 33

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start((1./18.)*90+2)

for i in range(0, 20):
    pwm.ChangeDutyCycle((1./18.)*100+2)
    time.sleep(0.02)
    
pwm.ChangeDutyCycle(3.0)
time.sleep(1.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()
