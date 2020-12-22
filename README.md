# biometric_authentication

# STEP1:

#Installations

The installation process for this project is a bit more than usual. First we have to download a C++ compiler. We can do this by installing Visual Studios. You can download the community version for free from their website. Once the intaller we will run it and select the ‘Desktop development with C++’.

#install the required packages. Below is the list.

* cmake
* dlib
* face_recognition
* numpy
* opencv-python

# STEP2:
#Understanding the problem

Although many face recognition opencv algorithms have been developed over the years, their speed and accuracy balance has not been quiet optimal . But some recent advancements have shown promise. A good example is Facebook, where they are able to tag you and your friends with just a few images of training and with accuracy as high as 98%. So how does this work . This repo is replicating similar results using a face recognition library developed by Adam Geitgey.

# STEP3:
# FACE RECOGNITION
#Face recognition is a series of several problems:

* First, look at a picture and find all the faces in it
* Second, focus on each face and be able to understand that even if a face is turned in a weird direction or in bad lighting, it is still the same person.
* Third, be able to pick out unique features of the face that you can use to tell it apart from other people— like how big the eyes are, how long the face is, etc.
* Finally, compare the unique features of that face to all the people you already know to determine the person’s name.

*Step 1*
Loading Images and Converting to RGB.

*Step 2*
Find Faces Locations and Encodings.

*Step 3*
Compare Faces and Find Distance.


# STEP4:
# ATTENDANCE PROJECT
In this repo, I'll develop an attendance system where the user is automatically logged when they are detected in the camera. We will store the name along with the time when they appeared.

*Step 1*
Importing Images

*Step 2*
Compute Encodings

*Step 3*
The WHILE Loop contains:
* WebCam image
* webCam encodings
* Find Matches
* Marking Attendance for known persons

*Step 4*
FOR UNKNOWN PERSON:
(i.e)the person is unknown so we change the name to unknown and don’t mark the attendance.


# CONCLUTION
The face recognition opencv method is one of the easiest and fastest ways to implement the facial recognition.
