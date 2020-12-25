import numpy as np
import cv2
import os
import time

import json

import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

from string import ascii_lowercase

def findHands(image):
    image.flags.writeable = False
    return hands.process(image)


def show(image,color,results):
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    
    image.flags.writeable = True
    #frame = cv2.rectangle(frame,(frame.shape[1]//2-110,100),(frame.shape[1]//2+110,320),color,5)
    cv2.putText(image, caractere,(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)

    #image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('frame',image)


def makeDir(str):
    try:
        os.mkdir(str)
    except OSError:
        print ("Creation of the directory  failed" )
    else:
        print ("Successfully created the directory")



makeDir('DATASET')

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5,max_num_hands=1)

i = 0
writing = False
#jutsus=("passaro","porco","cachorro","dragao","coelho","cavalo","macaco","touro","carneiro","rato","cobra","tigre")
#options = ("pedra","papel","tesoura")#,"largato","spock","nada")
alfabeto = iter(ascii_lowercase)
caractere = next(alfabeto)
#makeDir('DATASET/'+caractere)
f = open('DATASET/'+caractere,"w")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("problemas recebendo frames da camera")
        continue
    
    # Display the resulting frame
    key = cv2.waitKey(33)
    if key == ord('s'):
        writing = True
        startTime = int(time.time())
        

    elif key & 0xFF == ord('q'):
        break

    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    results = findHands(frame)
    
    if results.multi_handedness != None:
        print(results.multi_handedness[0].classification[0].label)
        print(results.multi_hand_landmarks[0])
    if writing == True:
        print ("saving cropped frame to dataset")
        if i < 10:
            elapsed = int(time.time()) - startTime
            if elapsed < 3:
                cv2.putText(frame, "saving in "+str(3-elapsed),(200, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)
                show(frame,(0,0,255),results)

            else:
                startTime = int(time.time())
                for j in range(10):
                    ret, frame = cap.read()
                    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
                    results = findHands(frame)
                    show(frame,(0,0,255),results)
                    #f.write(results.multi_handedness[0].classification[0].label)
                    #print(type(list(results.multi_hand_landmarks)))
                    l = list(map(lambda x: str(x),results.multi_hand_landmarks))
                    jstr = json.dumps(l, indent=4)
                    f.write(jstr)
                i += 1
        else:
            i = 0
            writing = False
            caractere = next(alfabeto)
            f.close()
            f = open('DATASET/'+caractere,"w")
            #makeDir('DATASET/'+caractere)	
    else:
        show(frame,(255,255,255),results)

# When everything done, release the capture
f.close()
hands.close()
cap.release()
cv2.destroyAllWindows()