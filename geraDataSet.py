import numpy as np
import cv2
import os
import time

from string import ascii_lowercase


def show(frame,color):
    frame = cv2.rectangle(frame,(frame.shape[1]//2-110,100),(frame.shape[1]//2+110,320),color,5)
    cv2.putText(frame, caractere,(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)

    cv2.imshow('frame',frame)

def makeDir(str):
    try:
        os.mkdir(str)
    except OSError:
        print ("Creation of the directory  failed" )
    else:
        print ("Successfully created the directory")



makeDir('DATASET')

cap = cv2.VideoCapture(0)


i = 0
writing = False
#jutsus=("passaro","porco","cachorro","dragao","coelho","cavalo","macaco","touro","carneiro","rato","cobra","tigre")
options = ("pedra","papel","tesoura")#,"largato","spock","nada")
alfabeto = iter(options)
caractere = next(alfabeto)
makeDir('DATASET/'+caractere)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Display the resulting frame
    key = cv2.waitKey(33)
    if key == ord('s'):
        writing = True
        startTime = int(time.time())
        

    elif key & 0xFF == ord('q'):
        break

    if writing == True:
        print ("saving cropped frame to dataset")
        if i < 10:
            elapsed = int(time.time()) - startTime
            if elapsed < 3:
                cv2.putText(frame, "saving in "+str(3-elapsed),(200, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)
                show(frame,(0,0,255))

            else:
                startTime = int(time.time())
                for j in range(10):
                    ret, frame = cap.read()
                    #frame = cv2.circle(frame,(50,100),10,(255,255,255),-1)
                    #cv2.putText(frame, "saving",(200, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0),2,cv2.LINE_4)

                    #show(frame,(0,0,255))
                    cv2.imshow('frame',frame)
                    frame = frame[100:320,frame.shape[1]//2-110:frame.shape[1]//2+110]
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite('DATASET/'+caractere+'/'+str(i)+'-'+str(j)+'.jpg',frame)
                i += 1
        else:
            i = 0
            writing = False
            caractere = next(alfabeto)
            makeDir('DATASET/'+caractere)	
    else:
        show(frame,(255,255,255))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()