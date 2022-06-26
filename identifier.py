import cv2
import face_recognition
from transliterate import translit, get_available_language_codes

def identifier(photo, data,area):
    embedingSet = []
    # print(data)
    for id in data:
        # print(id)
        embedingSet.append(data[id][1])
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
            fio = data[id][0]
            fio = translit(fio, 'ru', reversed=True)
            name = False
            rect = cv2.rectangle(
                photo,  (area[0][1], area[0][0]), (area[0][3], area[0][2]), (0, 255, 0), thickness=3)
            if(fio):
                print(fio)
                cv2.putText(
                    photo, fio, (area[0][3], area[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1)
            return(rect)
    else:
        return photo




