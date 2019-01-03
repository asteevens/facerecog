#Author: Shantnu Tiwari
#Source: https://realpython.com/face-recognition-with-python/
#Modified by asteevens 3/12/18
#Final Project for CPT-135-N01-18/FA


import cv2
import sys
import easygui
from tkinter import *
import os

#Astee - Setting globals for file metadata to load into list/dictionary/tupples
fileSize = []


# Get user supplied values
# Astee - added filedialog window function with easygui

def OpenWC():
    #Astee - open webcam function
    
    cap = cv2.VideoCapture(0)

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                    #flags = cv2.CV_HAAR_SCALE_IMAGE
            )

            print("Found {0} faces!".format(len(faces)))

            #Astee - pushing data to log file for Webcam process

            logCreate = open("WebCamLogFile.txt", "w+")

            logCreate.write("Found {0} faces!".format(len(faces)))

            logCreate.close()

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


def FileDiag():
    #Astee - open file function

    imagePath = easygui.fileopenbox()
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)

    #Astee - Store filename and file size to global list

    filePath = imagePath

    imageSize = os.path.getsize(imagePath)

    fileSize.append(filePath)

    fileSize.append(imageSize)

    print(fileSize)

    
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

    #Astee - status for text pane

    statusPane = ("Found {0} faces!".format(len(faces)))

    #Astee - writing to log file for image import process

    logCreate2 = open("ImageImportLogFile.txt", "w+")

    logCreate2.write("Found {0} faces!".format(len(faces)))

    logCreate2.close()

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

    #Astee - write status of face recog to text pane

    T = Text(root, height=2, width=30)
    T.pack()
    quote = statusPane
    T.insert(END, quote)

def ShowCredits():
    #Astee - read from text file to display source info

    viewCredits = open("Credits.txt", "r+")

    loadCredits = viewCredits.readlines()

    easygui.textbox(msg='', title='View Credits', text=loadCredits, codebox=0)

    viewCredits.close()

def KillApp():
    #Astee - quit button in ui
    sys.exit()
    
    
    
#Astee - building ui


root = Tk()
root.configure(background='black')
frame = Frame(root)
frame.pack()

root.title("Facial Recognition")

root.geometry("850x650")

BGImg = PhotoImage(file = "BgImg.png")
background_label = Label(image=BGImg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

topframe = Frame(root)
topframe.pack(side=TOP)

button1 = Button(topframe, padx=16, pady = 16, bd =9, text="Select a Photo From Your Computer", fg="black", command=FileDiag)
button1.pack(side=LEFT)

button2 = Button(topframe, padx=16, pady = 16, bd =8, text="Open Webcam to Scan for Faces (Press 'Q' to quit while scan is in progress.)", fg="black", command=OpenWC)
button2.pack(side=RIGHT)

button3 = Button(topframe, padx=16, pady = 16, bd =8, text="Credits", fg="black", command=ShowCredits)
button3.pack(side=RIGHT)

button4 = Button(topframe, padx=16, pady = 16, bd =8, text="Quit", fg="black", command=KillApp)
button4.pack(side=RIGHT)


#AStee - end of root
root.mainloop()
