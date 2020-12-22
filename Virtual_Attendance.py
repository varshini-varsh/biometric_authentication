# Coded by Varshini

# STEP1:
#Importing libraries

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#STEP2:
#Importing image dataset in the path named "ImagesAttendance"

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
# Print all image(.jpg) in the path
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# Print all names in the path
print(classNames)

# STEP3:
# Computing encodings

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
# STEP4:
#Marking Attendance

def markAttendance(name):

    # Marking attendance in "Attendance.csv"
    
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

# Callingthe function with image list

encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Turn on WebCam Image

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    # img resizing
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    
    # Turn BGR Image to RGB Image
    
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # WebCam Encodings
    
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)


    # Find Matches
    
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        
        # Once list of face distance found, find the maximum ine as this would be the best match
        matchIndex = np.argmin(faceDis)
        
        # Based on index value, determine the name of the person and display it on the original image
        
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            markAttendance(name)
            
        #  for Unkown faces detection
        
        else:
            name = "Unknown"
            
            #print(name)
            
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    # show image in webcam
    
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
