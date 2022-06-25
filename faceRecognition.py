import cv2
import face_recognition
from resize import image_resize

#img = cv2.imread('./src/img/faces4.jpg')
#grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#faces = cv2.CascadeClassifier('./src/models/faces.xml')



def faceRecognition(cap):
    while True:
        success, img = cap.read()
        # print(img)
        img = image_resize(img, height=240)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        area = face_recognition.face_locations(rgb, model='hog')
        output=img
        if(area):
            rect = img
            output = cv2.rectangle(
                rect,  (area[0][2], area[0][3]), (area[0][0], area[0][1]),(0, 0, 255), thickness=2)
            #print(area)
            #grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # print(grayImg)
            # cv2.imshow('1', output)
            # cv2.waitKey(0)
            face = img[area[0][0]:area[0][1], area[0][3]:area[0][2]]
            return img

        if cv2.waitKey(66) & 0xFF == ord('q'):
            break




