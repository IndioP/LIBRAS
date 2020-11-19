import cv2
#from fastai import *
#from fastai import load_learner
#import torch
from fastbook import *
from fastai.vision.widgets import *


#fastai.basics.defaults.device = torch.device('cpu')
#defaults.device = torch.device('cpu')
#learn_inf = load_learner('modelo/')
#print(learn_inf.dls.vocab)
path = Path()
path.ls(file_exts='.pkl')
learn_inf = load_learner(path/'export.pkl')
learn_inf.dls.vocab
#pred,pred_idx,probs = learn_inf.predict(img)

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    frame = frame[100:320,frame.shape[1]//2-110:frame.shape[1]//2+110]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pred,pred_idx,probs = learn_inf.predict(frame)
    #hide_output
    lbl_pred = widgets.Label()
    if probs[pred_idx] > 0.8:
        lbl_pred.value = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'
    print(lbl_pred)
    cv2.imshow('frame',frame)
    # Display the resulting frame
    key = cv2.waitKey(33)

    if key & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()