
# Face Recognition Bases Attendence System


In this project, I am going to perform Facial recognition with high accuracy. I will create an Attendance project that will use webcam to detect faces and record the attendance live in an excel sheet.

## Features

- Loads Images and Converts into RGB.
- Find Faces Locations and Encodings
- Compare Faces and Find Distance
- Marks attendence in a excel sheet
- All this does is to check if the distance to our min face is less than 0.5 or not. If its not then this means the person is unknown so we change the name to unknown and don’t mark the attendance.


## Installation

```bash
  we have to download a C++ compiler. 
  We can do this by installing Visual Studios. 
  You can download the community version for free from their website. 
  Once the intaller we will run it and select the ‘Desktop development with C++’. 
```
```bash
After completing and restarting the computer, now we will head on to our Pycharm project in visual studio code. 
Here we will install the required packages. Below is the list.
 can be installed like- pip install cmake
 - cmake
 - dlib
 - face-recognition
 - numpy
 - opencv-python
 After installing the required packages, run "attendenceProject.py
 When you done taking the attendence press ctrl + c to stop the program and then open Attendence.csv to see attendence in excel file.
 
 NOTE:- I have uploaded images in tesimages folder, if you want to test it with your own images, 
 just add your image to testimages folder with yourname.jpg and that will be enough to detect your image, your image will gets added and ready for detection
 When you run the program, after encoding completed, you can see your image name in the Command Line."
```

### Here's How I have devided problem Statement
- First, look at a picture and find all the faces in it.
- Second, focus on each face and be able to understand that even if a face is turned in a weird direction or in bad lighting, it is still the same person.
- Third, be able to pick out unique features of the face that you can use to tell it apart from other people— like how big the eyes are, how long the face is, etc.
- compare the unique features of that face to all the people you already know to determine the person’s name.
- Finally, Mark the attendence.

#### Problems I faced And Solved Them
- My First Week- Since, I have never worked in the project like detecting faces from webcam, I was not sure how i am going to take data from webcam, how my program should work and what kind of features i should add.
  So I prefered so many articles available in the internet one of the article by Adam Geitgey https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78 helped me alot, so i have decided the face recognition LIBRARY developed by Adam. I planned the things accordingly, as my mentor inspired me to do.
  So my first week was like analyzing the problem, features i want to give, and figure out how i am going to do it

- My Second Week- Since I have planned things and analyzed the problem statement and determined the steps and tools i am going to use. I have started working on with the problem statement.
  Since I was very new to this thing, after reading few articles i come to know that i have to use OPENCV to detect faces, so i learned that from youtube and got to know how it works and can be implemented in my project.
  Since, i know python i started working and after converting images to RGB, I have used HOG algorithms, i was able to detect faces from the images provided and remove unwanted rotations. After that i moved to draw rectangles around the images. And here's how i have done that with just 2 lines of code, this was really interesting thing that i have learned, that the image is feed to a pretrained neural network that out puts 128 measurements that are unique to that particular face.
  ```bash
  encodeImage = face_recognition.face_encodings(image)&#91;0]
  cv2.rectangle(Image,(faceLoc&#91;3],faceLoc&#91;0]),(faceLoc&#91;1],faceLoc&#91;2]),(255,0,255),2) # top, ri
  ```
  After that, i was not sure how i am going to test whether the person is same as in our database or not, so i have learned how i can compare faces and distance, after getting encodings of the images
  i have used machine Learning method linear SVM classifier, This classifier works like it compares the distance between both images, If we run this with the test image we get the value True, indicating that the face found is of Image same as database image. The is done after measuring distance between the faces. The lower the distance the better the match.
  At the end of second week, i have done with face matching and taking the distance between the images.

- My Last Week- I have done with the image taking from webcam and checking it with data images that i have provided, now i started figuring out, that how i am going to mark attendence in the excel sheet,
  So i searched in the internet, saw some tutorial and got some idea that what i need to do, i asked one of my friend who actively works in machine learning projects and that was really helpful,
  i have marked attendence in csv file with name and date, and one thing i was still not sure that, suppose if a person who already marked present, if he again come in front of the camera then how my program react, whether it will add two entries of the same person, with different time or leave it, I want that my program should do nothing if a person come againg in front of the camera.
  and i have figured out how i am gonna do it. and at last, I tested it with some common celebrity images like elon_musk, bill gates etc. And i was happy, my program works totally fine.
  One thing that i wanna add, this program not only works for students but, it can be used anywhere for marking attendence like employees, factories and many more places. 
## Screenshots
<img width="958" alt="project" src="https://user-images.githubusercontent.com/51431920/170859795-6fd2dd15-1981-4247-9b52-cde58eb1cd15.png">
<img width="959" alt="project2" src="https://user-images.githubusercontent.com/51431920/170859853-8c3b7473-0c68-43ca-b164-a2093da9cce5.png">
<img width="945" alt="finally" src="https://user-images.githubusercontent.com/51431920/170859860-446fdd24-0c36-47e3-aa67-2b6a72299177.png">

# Future Of This Project
  Since, This project is ready to run, I mean it is so simple and can be used, you run it after connecting it with a camera, and that camera can be placed at the  entrance, and then it is ready to take attendence, mark peaople names along with time. Like for example you want to take attendence in a school, you place a camera in 
  the entrance of the class or floor, and run the program for say, you take attendence between 8:00 AM to 820 AM, after that terminate the program and voilla your
  excel file is ready with the names and time the student came.
  Sililarly. for parking area for employees, teacher attendence, factory workers, and it can be used anywhere.



