import cv2
import face_recognition
import numpy as np
import base64
import pickle

def identifier(photo, data,area):
    embedingSet = []
    # print(data)
    for id in data:
        # print(id)
        embedingSet.append(data[id])
    # print(embedingSet)
    rgb = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    if(not len(encodings)):
        return photo
    else:
        matches = face_recognition.compare_faces(
        embedingSet, encodings[0])

    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        for i in matchedIdxs:
            id = list(data.keys())[i]
            name = False
            rect = cv2.rectangle(
                photo,  (area[0][1], area[0][0]), (area[0][3], area[0][2]), (0, 255, 0), thickness=2)
            if(id == '1'):
                name = 'Nastya'
            if(id == '2'):
                name = 'Dima'
            if(id == '3'):
                name = 'Nikita'
            if(id == '4'):
                name = 'Nikita'
            if(id == '5'):
                name = 'Nikita'
            if(name):
                print(name)
                cv2.putText(
                    photo, name, (area[0][3], area[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)
            return(rect)
    else:
        return photo




