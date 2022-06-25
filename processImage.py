from faceRecognition import faceRecognitionFromPhoto
from identifier import identifier
from faceRecognition import faceRecognitionFromPhoto

import numpy as np

import cv2
import base64
import json

with open('face_enc.json', 'r') as jsonFile:
    data = json.load(jsonFile)
def processImage(frame:str):
    frame = base64.b64decode(frame)
    np_data = np.fromstring(frame, np.uint8)
    frame = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
    face = faceRecognitionFromPhoto(frame)
    if(len(face[2])):
        photo = identifier(face[1], data, face[2])
        photo = cv2.imencode('.png', photo)[1].tostring()
        encoded_string = base64.b64encode(photo)
        return(encoded_string)
    else:
        photo = cv2.imencode('.png', face[0])[1].tostring()
        encoded_string = base64.b64encode(photo)
        return(encoded_string)


