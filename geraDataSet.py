import numpy as np
import cv2
import os
import time

import csv

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
csv_file = open('DATASET/'+caractere+'.csv',"w")
f = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
f.writerow(["left_or_right","WRIST.x","WRIST.y","WRIST.z","THUMB_CMC.x","THUMB_CMC.y","THUMB_CMC.z","THUMB_MCP.x","THUMB_MCP.y","THUMB_MCP.z","THUMB_IP.x","THUMB_IP.y","THUMB_IP.z","THUMB_TIP.x","THUMB_TIP.y","THUMB_TIP.z","INDEX_FINGER_MCP.x","INDEX_FINGER_MCP.y","INDEX_FINGER_MCP.z","INDEX_FINGER_PIP.x","INDEX_FINGER_PIP.y","INDEX_FINGER_PIP.z","INDEX_FINGER_DIP.x","INDEX_FINGER_DIP.y","INDEX_FINGER_DIP.z","INDEX_FINGER_TIP.x","INDEX_FINGER_TIP.y","INDEX_FINGER_TIP.z","MIDDLE_FINGER_MCP.x","MIDDLE_FINGER_MCP.y","MIDDLE_FINGER_MCP.z","MIDDLE_FINGER_PIP.x","MIDDLE_FINGER_PIP.y","MIDDLE_FINGER_PIP.z","MIDDLE_FINGER_DIP.x","MIDDLE_FINGER_DIP.y","MIDDLE_FINGER_DIP.z","MIDDLE_FINGER_TIP.x","MIDDLE_FINGER_TIP.y","MIDDLE_FINGER_TIP.z","RING_FINGER_MCP.x","RING_FINGER_MCP.y","RING_FINGER_MCP.z","RING_FINGER_PIP.x","RING_FINGER_PIP.y","RING_FINGER_PIP.z","RING_FINGER_DIP.x","RING_FINGER_DIP.y","RING_FINGER_DIP.z","RING_FINGER_TIP.x","RING_FINGER_TIP.y","RING_FINGER_TIP.z","PINKY_MCP.x","PINKY_MCP.y","PINKY_MCP.z","PINKY_PIP.x","PINKY_PIP.y","PINKY_PIP.z","PINKY_DIP.x","PINKY_DIP.y","PINKY_DIP.z","PINKY_TIPPINKY_TIP.x","PINKY_TIPPINKY_TIP.y","PINKY_TIPPINKY_TIP.z"])
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
    

    if writing == True:
        print ("saving cropped frame to dataset")
        if i < 12:
            
            elapsed = int(time.time()) - startTime
            if elapsed < 3:
                cv2.putText(frame, "saving in "+str(3-elapsed),(200, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)
                show(frame,(0,0,255),results)

            else:
                startTime = int(time.time())
                
                if results.multi_handedness != None:
                    points = [results.multi_handedness[0].classification[0].label]
                    for l in results.multi_hand_landmarks[0].landmark:
                        points.append(l.x)
                        points.append(l.y)
                        points.append(l.z)
                    f.writerow(points)
                    writing = False
                    i += 1
        else:
            i = 0
            writing = False
            caractere = next(alfabeto)
            csv_file.close()
            csv_file = open('DATASET/'+caractere+'.csv',"w")
            f = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            f.writerow(["left_or_right","WRIST.x","WRIST.y","WRIST.z","THUMB_CMC.x","THUMB_CMC.y","THUMB_CMC.z","THUMB_MCP.x","THUMB_MCP.y","THUMB_MCP.z","THUMB_IP.x","THUMB_IP.y","THUMB_IP.z","THUMB_TIP.x","THUMB_TIP.y","THUMB_TIP.z","INDEX_FINGER_MCP.x","INDEX_FINGER_MCP.y","INDEX_FINGER_MCP.z","INDEX_FINGER_PIP.x","INDEX_FINGER_PIP.y","INDEX_FINGER_PIP.z","INDEX_FINGER_DIP.x","INDEX_FINGER_DIP.y","INDEX_FINGER_DIP.z","INDEX_FINGER_TIP.x","INDEX_FINGER_TIP.y","INDEX_FINGER_TIP.z","MIDDLE_FINGER_MCP.x","MIDDLE_FINGER_MCP.y","MIDDLE_FINGER_MCP.z","MIDDLE_FINGER_PIP.x","MIDDLE_FINGER_PIP.y","MIDDLE_FINGER_PIP.z","MIDDLE_FINGER_DIP.x","MIDDLE_FINGER_DIP.y","MIDDLE_FINGER_DIP.z","MIDDLE_FINGER_TIP.x","MIDDLE_FINGER_TIP.y","MIDDLE_FINGER_TIP.z","RING_FINGER_MCP.x","RING_FINGER_MCP.y","RING_FINGER_MCP.z","RING_FINGER_PIP.x","RING_FINGER_PIP.y","RING_FINGER_PIP.z","RING_FINGER_DIP.x","RING_FINGER_DIP.y","RING_FINGER_DIP.z","RING_FINGER_TIP.x","RING_FINGER_TIP.y","RING_FINGER_TIP.z","PINKY_MCP.x","PINKY_MCP.y","PINKY_MCP.z","PINKY_PIP.x","PINKY_PIP.y","PINKY_PIP.z","PINKY_DIP.x","PINKY_DIP.y","PINKY_DIP.z","PINKY_TIPPINKY_TIP.x","PINKY_TIPPINKY_TIP.y","PINKY_TIPPINKY_TIP.z"])
            #makeDir('DATASET/'+caractere)	
    else:
        show(frame,(255,255,255),results)

# When everything done, release the capture
csv_file.close()
hands.close()
cap.release()
cv2.destroyAllWindows()