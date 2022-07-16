# -*- coding: utf-8 -*-

import numpy as np
import cv2

xml = 'haarcascade_frontface.xml'
face_cascade = cv2.CascadeClassifier(xml) #사전학습데이터 불러오기

cap = cv2.VideoCapture(-1) #카메라 번호(바뀔 수 있음) 
ret, frame = cap.read()


cap.set(3,640)
cap.set(4,480)
facelen = 0
facedelay = 0


while(True):
    ret, frame = cap.read() #카메라에서 프레임 읽어오기
    frame = cv2.flip(frame, 1) #카메라에서 읽어온 프레임 좌우반전
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) #카메라에서 읽어온 프레임 회전해서 표시
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cvt color 함수로 gray로 추출

    faces = face_cascade.detectMultiScale(gray, 1.05, 5) #학습데이터 기반 얼굴 검출(프레임, 스케일팩터, 선두께 지정)
    facelen = str(len(faces))
    facelenint=int(facelen)
    print("Number of faces detected: " + facelen)

    if len(faces):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0), 5)
        
    cv2.imshow('FACEID', frame)#카메라 영상 프레임으로 새창 열어 표시

    
    if facelenint != 0:
        facedelay += 1
        print('delay')
        print(facedelay)
    else:
        facedelay = 0
    
    if facedelay == 10:
        exec(open("RSID_Authenticate.py").read())
        facedelay = 0

    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()

 
