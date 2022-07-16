"""
License: Apache 2.0. See LICENSE file in root directory.
Copyright(c) 2020-2021 Intel Corporation. All Rights Reserved.
"""

import rsid_py
import time
import Jetson.GPIO as GPIO
SERVO_PIN = 33

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start((1./18.)*90+2)


PORT='/dev/ttyACM0'

def on_result(result, user_id):
    print('on_result', result)    
    if result == rsid_py.AuthenticateStatus.Success:
        print('Authenticated user:', user_id)
        exec(open("RSID_Unlock.py").read())
        print('unlocked')


def on_faces(faces, timestamp):    
    print(f'detected {len(faces)} face(s)')
    for f in faces:
        print(f'\tface {f.x},{f.y} {f.w}x{f.h}')    

if __name__ == '__main__':
    with rsid_py.FaceAuthenticator(PORT) as f:
        f.authenticate(on_faces=on_faces, on_result=on_result)
