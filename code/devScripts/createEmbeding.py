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
    fio = dict['fio']
    encArr = []

    decoded_data = base64.b64decode(photo)
    np_data = np.fromstring(decoded_data,np.uint8)
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    area = face_recognition.face_locations(rgb, model='hog')

    encodings = face_recognition.face_encodings(rgb, area)

    if(len(encodings)>1 or not len(encodings)):
        return False
    else:
        return {id:[fio,encodings[0].tolist()]} 
    # cv2.imshow("test", img)
    # cv2.waitey(0)


def createFile(dict):
    with open(".../data/face_enc.json", "w") as outfile:
        outfile.write(json.dumps(dict))

def addLocalUser(dict):
    with open('.../data/face_enc.json', 'r') as jsonFile:
        jsonOut = json.load(jsonFile)
        # print(jsonOut['40'])
        id = list(dict.keys())[0]
        # print(id)
        jsonOut[id] = []
        jsonOut[id].append(dict[id][0])
        jsonOut[id].append(dict[id][1])
        # print(jsonOut[id][0])
        with open(".../data/face_enc.json", "w") as outfile:
            outfile.write(json.dumps(jsonOut))


# with open("./faces/nikita.jpeg", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#     id = randint(0,100)
#     dict = {'id':id,'photo':encoded_string}
#     dictToWrite = createEmbeding(dict)
#     addLocalUser(dictToWrite)
#     # print(dictToWrite)
def updateLocalUsers():
    with open(".../data/local.json", "r") as localIn:
        localJson = json.load(localIn)
        localJsonKeys = list(localJson.keys())
        for id in localJsonKeys:
            # print(id)
            dict = {}
            # dict[id] = []
            # dict[id].append(localJson[id][0])
            # dict[id].append(localJson[id][1])
            dict["id"] = id
            dict["fio"] = localJson[id][0]
            dict["photo"] = localJson[id][1]
        # dict = {'id':id,'photo':encoded_string}
            dictToWrite = createEmbeding(dict)
            if(dictToWrite):
                print(dictToWrite[id][0])
                addLocalUser(dictToWrite)
        # print(dictToWrite)

# def updateLocalUsers():
#     with open("./local.json", "r") as localIn:
#         localJson = json.load(localIn)
#         localJsonKeys = list(localJson.keys())
#         dict = {}
#         dict["id"] = id
#         dict["fio"] = localJson[id][0]
#         dict["photo"] = localJson[id][1]
#         # dict = {'id':id,'photo':encoded_string}
#         dictToWrite = createEmbeding(dict)
#         if(dictToWrite):
#             print(dictToWrite[id][0])
#             addLocalUser(dictToWrite)
#     # print(dictToWrite)

# updateLocalUsers()
