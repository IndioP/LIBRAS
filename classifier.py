import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

from fastai.tabular.all import *
#from fastai.tabular.widgets import *


path = Path()
path.ls(file_exts='.pkl')
learn_inf = load_learner(path/'modeloTabular.pkl')
vocab = learn_inf.dls.vocab
print(vocab)


df = pd.read_csv('fullDATASET.csv')
df.head()


# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5,max_num_hands=1)
cap = cv2.VideoCapture(0)
while cap.isOpened():
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    # If loading a video, use 'break' instead of 'continue'.
    continue

  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
  image.flags.writeable = False
  results = hands.process(image)
  points = []
  if results.multi_handedness != None:
    points.append(results.multi_handedness[0].classification[0].label)
    for l in results.multi_hand_landmarks[0].landmark:
      points.append(l.x)
      points.append(l.y)
      points.append(l.z)
  #print(points)
  lista = ["left_or_right","WRIST.x","WRIST.y","WRIST.z","THUMB_CMC.x","THUMB_CMC.y","THUMB_CMC.z","THUMB_MCP.x","THUMB_MCP.y","THUMB_MCP.z","THUMB_IP.x","THUMB_IP.y","THUMB_IP.z","THUMB_TIP.x","THUMB_TIP.y","THUMB_TIP.z","INDEX_FINGER_MCP.x","INDEX_FINGER_MCP.y","INDEX_FINGER_MCP.z","INDEX_FINGER_PIP.x","INDEX_FINGER_PIP.y","INDEX_FINGER_PIP.z","INDEX_FINGER_DIP.x","INDEX_FINGER_DIP.y","INDEX_FINGER_DIP.z","INDEX_FINGER_TIP.x","INDEX_FINGER_TIP.y","INDEX_FINGER_TIP.z","MIDDLE_FINGER_MCP.x","MIDDLE_FINGER_MCP.y","MIDDLE_FINGER_MCP.z","MIDDLE_FINGER_PIP.x","MIDDLE_FINGER_PIP.y","MIDDLE_FINGER_PIP.z","MIDDLE_FINGER_DIP.x","MIDDLE_FINGER_DIP.y","MIDDLE_FINGER_DIP.z","MIDDLE_FINGER_TIP.x","MIDDLE_FINGER_TIP.y","MIDDLE_FINGER_TIP.z","RING_FINGER_MCP.x","RING_FINGER_MCP.y","RING_FINGER_MCP.z","RING_FINGER_PIP.x","RING_FINGER_PIP.y","RING_FINGER_PIP.z","RING_FINGER_DIP.x","RING_FINGER_DIP.y","RING_FINGER_DIP.z","RING_FINGER_TIP.x","RING_FINGER_TIP.y","RING_FINGER_TIP.z","PINKY_MCP.x","PINKY_MCP.y","PINKY_MCP.z","PINKY_PIP.x","PINKY_PIP.y","PINKY_PIP.z","PINKY_DIP.x","PINKY_DIP.y","PINKY_DIP.z","PINKY_TIPPINKY_TIP.x","PINKY_TIPPINKY_TIP.y","PINKY_TIPPINKY_TIP.z"]
  
  if len(points) == 64:
    inputPoints = pd.DataFrame([points],columns=["left_or_right","WRIST.x","WRIST.y","WRIST.z","THUMB_CMC.x","THUMB_CMC.y","THUMB_CMC.z","THUMB_MCP.x","THUMB_MCP.y","THUMB_MCP.z","THUMB_IP.x","THUMB_IP.y","THUMB_IP.z","THUMB_TIP.x","THUMB_TIP.y","THUMB_TIP.z","INDEX_FINGER_MCP.x","INDEX_FINGER_MCP.y","INDEX_FINGER_MCP.z","INDEX_FINGER_PIP.x","INDEX_FINGER_PIP.y","INDEX_FINGER_PIP.z","INDEX_FINGER_DIP.x","INDEX_FINGER_DIP.y","INDEX_FINGER_DIP.z","INDEX_FINGER_TIP.x","INDEX_FINGER_TIP.y","INDEX_FINGER_TIP.z","MIDDLE_FINGER_MCP.x","MIDDLE_FINGER_MCP.y","MIDDLE_FINGER_MCP.z","MIDDLE_FINGER_PIP.x","MIDDLE_FINGER_PIP.y","MIDDLE_FINGER_PIP.z","MIDDLE_FINGER_DIP.x","MIDDLE_FINGER_DIP.y","MIDDLE_FINGER_DIP.z","MIDDLE_FINGER_TIP.x","MIDDLE_FINGER_TIP.y","MIDDLE_FINGER_TIP.z","RING_FINGER_MCP.x","RING_FINGER_MCP.y","RING_FINGER_MCP.z","RING_FINGER_PIP.x","RING_FINGER_PIP.y","RING_FINGER_PIP.z","RING_FINGER_DIP.x","RING_FINGER_DIP.y","RING_FINGER_DIP.z","RING_FINGER_TIP.x","RING_FINGER_TIP.y","RING_FINGER_TIP.z","PINKY_MCP.x","PINKY_MCP.y","PINKY_MCP.z","PINKY_PIP.x","PINKY_PIP.y","PINKY_PIP.z","PINKY_DIP.x","PINKY_DIP.y","PINKY_DIP.z","PINKY_TIPPINKY_TIP.x","PINKY_TIPPINKY_TIP.y","PINKY_TIPPINKY_TIP.z"])
    #print(inputPoints)
    #inputPoints.to_csv('city.csv')
    
    
    pred,pred_idx,probs = learn_inf.predict(inputPoints.iloc[0])
    
    
    #hide_output
    #lbl_pred = widgets.Label()
    #if probs[pred_idx] > 0.8:
    #    lbl_pred.value = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'
    #print(lbl_pred)
    
    
    
    print(vocab[pred_idx])

  # Draw the hand annotations on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
  cv2.imshow('MediaPipe Hands', image)
  if cv2.waitKey(5) & 0xFF == 27:
    break
hands.close()
cap.release()