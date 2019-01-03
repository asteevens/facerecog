#Author: Shantnu Tiwari
#Source: https://realpython.com/face-recognition-with-python/
#Modified by asteevens 3/12/18


import cv2
import sys
import easygui
from tkinter import *

#building ui

root = Tk()
frame = Frame(root)
frame.pack()

root.title("Facial Recognition")

num1=StringVar()

topframe = Frame(root)
topframe.pack(side=TOP)

txtDisplay=Entry(frame, textvariable = num1, bd =20, insertwidth =1, font=30)

txtDisplay.pack(side=TOP)

button1 = Button(topframe, padx=16, pady = 16, bd =8, text="Select a Photo From Your Computer", fg="black",)
button1.pack(side=LEFT)


# Get user supplied values
# Astee - added filedialog window




imagePath = easygui.fileopenbox()
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
