In this project, I am going to perform Facial recognition with high accuracy. I will create an Attendance project that will use webcam to detect faces and record the attendance live in an excel sheet.

Dependencies Used:- 
CMAKE
DLIB
FACE_RECOGNITION
OPEN CV PYTHON

This project is devided into three steps:-
1. making backend using python where i will match the images with the encodings, that image will come from web cam
Since, we are doing it in real time,  i have reduced our image size to 1/4th of the original image
Next, After observing that the correct match has minimum face distance in the results, when i was printing it, so out of several images , only the least face distance image will be the matching image.
After that i have marked attendence in excel sheet with name and timing.
And if someone who have already marked present, and if he/she tries to come again, then it will do nothing.

2. in this step i have build an api in order to link the backend part with front-end and make it usable.

3. Polish the web app and add features like graphs using the csv file for student performance.