# Attendence Management system via Face Recognition
# Importing the libraries
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pywhatkit
import multiprocessing

path = 'Training_images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name, number):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{name},{dtString}\n')
            pywhatkit.sendwhatmsg("+91"+number, "Attendance of "+name+" marked at " +
                                  dtString, datetime.now().hour, datetime.now().minute + 1)
def main():
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Face Detection')
    while True:
        _, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        # Converting the video to RGB
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        # Comparing the encodings
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            # If the face matches
            if matches[matchIndex]:
                name = classNames[matchIndex].split("_")[0].upper()
                number = classNames[matchIndex].split("_")[1]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                cv2.rectangle(img, (x1, y2-35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                # Marking the attendance
                markAttendance(name, number)
        # Displaying the video
        cv2.imshow('Face Detection', img)
        if cv2.waitKey(1) == ord('q'):
            break

    # Releasing the video
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


