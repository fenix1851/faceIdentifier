import cv2
import face_recognition
from resize import image_resize

#img = cv2.imread('./src/img/faces4.jpg')
#grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#faces = cv2.CascadeClassifier('./src/models/faces.xml')



def faceRecognition(cap):
    while True:
        print(1)
        success, img = cap.read()
        # print(img)
        img = image_resize(img, height=180)
        # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        area = face_recognition.face_locations(rgb, model='hog')
        print(area)
        output=img
        rect=[]
        if(area):
            rect = img
            output = cv2.rectangle(
                rect,  (area[0][1], area[0][0]), (area[0][3], area[0][2]),(0, 0, 255), thickness=2)
            return (img, rect,area)
        else:
            return(img,[],area)

        if cv2.waitKey(66) & 0xFF == ord('q'):
            break

def faceRecognitionFromPhoto(photo):
    img = image_resize(photo, height=180)
    # rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    area = face_recognition.face_locations(rgb, model='hog')
    # print(area)
    output = img
    rect = []
    if(area):
        rect = img
        output = cv2.rectangle(
            rect,  (area[0][1], area[0][0]), (area[0][3], area[0][2]), (0, 255, 0), thickness=2)
        return (img, rect, area)
    else:
        return(img, rect, area)



