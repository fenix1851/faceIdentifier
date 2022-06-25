from faceRecognition import faceRecognition
from identifier import identifier

import cv2
import json

cap = cv2.VideoCapture('./videos/dima.mp4')
with open('face_enc.json', 'r') as jsonFile:
    data = json.load(jsonFile)
while True:
    face = faceRecognition(cap)
    if(len(face)):
        identifier(face,data)


