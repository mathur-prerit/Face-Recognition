#User dataset input file

import cv2
import os
import time

#Capturing images
def cam_capture():
    path = "dataset/train/"
    name=input('Enter name of the user')
    if os.path.exists(path+name)==False:
        print('Creating new directory')
        os.mkdir(path+name)
    elif os.path.exists(path+name)==True:
        print("Folder already existed,replacing files")
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam=cv2.VideoCapture(0)
    samplenum=1
    while (cam.isOpened()):
        ret, frame = cam.read()
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(samplenum)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        imgf = cv2.resize(frame[y:y+h,x:x+w], (300, 300))
        cv2.imwrite(path + name + '/' + name + str(samplenum) + '.jpg', imgf)
        cv2.imshow('Frames', frame)
        time.sleep(1)
        samplenum = samplenum + 1
        cv2.waitKey(10)
        if samplenum>100:
            break
        print("Dataset created successfully")
        '''if cv2.waitKey(1) & 0xFF == ord('q'):
            break'''
    cam.release()
    cv2.destroyAllWindows()





