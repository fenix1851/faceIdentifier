import cv2
import face_recognition
import numpy as np
import base64
import pickle

def identifier(photo, data):
    embedingSet = []
    # print(data)
    for id in data:
        # print(id)
        embedingSet.append(data[id])
    # print(embedingSet)
    rgb = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    if(not len(encodings)):
        return False
    else:
        matches = face_recognition.compare_faces(
        embedingSet, encodings[0])

    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        for i in matchedIdxs:
            id = list(data.keys())[i]
            if(id == '1'):
                print('Nastya')
            if(id == '2'):
                print('Dima')
            if(id == '3'):
                print('Nikita')
            if(id == '4'):
                print('Kristina')
            if(id == '5'):
                print('Kristina')


