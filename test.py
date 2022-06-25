from faceRecognition import faceRecognition
from identifier import identifier

import cv2
import json

cap = cv2.VideoCapture(0)
with open('face_enc.json', 'r') as jsonFile:
    data = json.load(jsonFile)
while True:
    face = faceRecognition(cap)
    if(len(face[2])):
        cv2.destroyWindow('Show')
        photo = identifier(face[1],data,face[2])
        cv2.imshow('1', photo)
        cv2.waitKey(66)
    else: 
        cv2.imshow('Show', face[0])
        cv2.waitKey(66)

        

