from random import randint
from venv import create
import cv2 
import face_recognition
import numpy as np
import base64

import json
import pickle

def createEmbeding(dict):
    photo = dict['photo']
    id = dict['id']
    encArr = []
    decoded_data = base64.b64decode(photo)
    np_data = np.fromstring(decoded_data,np.uint8)
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    area = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, area)
    if(len(encodings)>1):
        return False
    else:
        return {id:encodings[0].tolist()} 
    # cv2.imshow("test", img)
    # cv2.waitey(0)


def createFile(dict):
    with open("face_enc.json", "w") as outfile:
        outfile.write(json.dumps(dict))

def addLocalUser(dict):
    with open('face_enc.json', 'r') as jsonFile:
        jsonOut = json.load(jsonFile)
        # print(jsonOut['40'])
        id = list(dict.keys())[0]
        print(id)
        jsonOut[id] = dict[id]
        print(jsonOut)
        with open("face_enc.json", "w") as outfile:
            outfile.write(json.dumps(jsonOut))


# with open("./faces/nikita.jpeg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     id = randint(0,100)
#     dict = {'id':id,'photo':encoded_string}
#     dictToWrite = createEmbeding(dict)
#     addLocalUser(dictToWrite)
#     # print(dictToWrite)


