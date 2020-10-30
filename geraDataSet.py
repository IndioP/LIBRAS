import numpy as np
import cv2
import os

from string import ascii_lowercase

try:
    os.mkdir('DATASET')
except OSError:
    print ("Creation of the directory  failed" )
else:
    print ("Successfully created the directory")

cap = cv2.VideoCapture(0)


i = 0

alfabeto = iter(ascii_lowercase)
caractere = next(alfabeto)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.rectangle(frame,(100,200),(350,450),(255,255,255),10)
    cv2.putText(frame, caractere,(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)

    cv2.imshow('frame',frame)
    
    # Display the resulting frame
    key = cv2.waitKey(33)
    if key == ord('s'):
   		print "saving cropped frame to dataset"
   		for i in range(10):
   			for _ in range(4):
				ret, frame = cap.read()
			frame = cv2.rectangle(frame,(100,200),(350,450),(255,255,255),10)
			cv2.putText(frame, caractere,(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 255),2,cv2.LINE_4)

			cv2.imshow('frame',frame)

			frame = frame[200:450,100:350]
			cv2.imwrite('DATASET/'+caractere+str(i)+'.jpg',frame)
			i += 1
		i = 0	
		caractere = next(alfabeto)

    elif key & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()