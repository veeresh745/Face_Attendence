import cv2
import numpy as np
import face_recognition

# Load the jpg file into a numpy array
imgElon = face_recognition.load_image_file('testimages/elon_musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

# Find all facial features in all the faces in the image
imgTest = face_recognition.load_image_file('testimages/test_elon.jpg')
imgTest= cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

#finding encodings and making rectangle on main image face
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]),(255,0,255),2)

#finding encodings and making rectangle on test image face
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeElon_test = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1], faceLocTest[2]),(255,0,255),2)

#comparing these faces and finding distance between them using linear svm
results = face_recognition.compare_faces([encodeElon], encodeElon_test)
faceDis = face_recognition.face_distance([encodeElon], encodeElon_test)
print(results,faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)


#Use the local binary pattern histogram to detect the faces
cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon test', imgTest)
cv2.waitKey(0)