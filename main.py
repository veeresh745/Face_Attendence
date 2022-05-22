import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('testimages/elon_musk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('testimages/test_elon.jpg')
imgTest= cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon test', imgTest)
cv2.waitKey(0)