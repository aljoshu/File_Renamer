import os
import cv2 as cv
from tkinter import *
import tkinter as tk
import PIL.ImageTk
import PIL.Image

# Variables
pictsDirectory = 'pictures'
stdWidth = 600
stdHeight = 600
stdSize = (stdWidth, stdHeight)
current = 0
allPicts = []

# Iterate through each file in the 'pictures' directory
for filename in os.listdir(pictsDirectory):
  if("DS_Store" in filename):
    print("Invalid File Found!")
  else:
    fullName = os.path.join(pictsDirectory, filename) # pictures/example.jpg
    allPicts.append(fullName)

root = tk.Tk()                        # m is the name of the main window
root.title('File Renamer')
frame = Frame(root)                   # use frame as the widget container
frame.pack()
bottomframe = Frame(root)             # make a frame at the bottom for allignment
bottomframe.pack(side=BOTTOM)

nameVar = tk.StringVar()
def submit():
  oldName = allPicts[current]
  newName = nameVar.get()
  extension = oldName.split(".")
  newName = "pictures/" + newName + "." + extension[1]
  if(len(newName) != 0):
    print("The new name for [" + oldName + "] is : " + newName)
    os.rename(oldName, newName)
    nameVar.set("")
    title.config(text=allPicts[current])


title = tk.Label(frame, text=allPicts[current], fg='red')    # Prints the current picture name
title.pack()

currImg = PIL.Image.open(allPicts[current])           # Open the current picture
ogWidth, ogHeight = currImg.size
aspRat = ogWidth / ogHeight
newRat = stdWidth / stdHeight
if(newRat > aspRat):
  resizeWidth = stdWidth
  resizeHeight = round(resizeWidth * aspRat)
else:
  resizeHeight = stdHeight
  resizeWidth = round(resizeHeight / aspRat)
currImg = currImg.resize((resizeWidth, resizeHeight))  # Resize the image to our liking
photoImg = PIL.ImageTk.PhotoImage(currImg)
imageLabel = tk.Label(image=photoImg)                 # Put the image in a Label widget
imageLabel.image = photoImg
imageLabel.pack()

indexStr = str(current + 1) + "/" + str(len(allPicts))
def next():
  global current, stdHeight, stdWidth
  # update the picture index value
  if(current < len(allPicts) - 1):
    current += 1
    updateIndex = str(current + 1) + "/" + str(len(allPicts))
    pictIndex.config(text=updateIndex)
    title.config(text=allPicts[current])
    #print("current index: " + updateIndex)

  # update the current display picture
  nextImg = PIL.Image.open(allPicts[current])
  ogWidth, ogHeight = currImg.size
  aspRat = ogWidth / ogHeight
  newRat = stdWidth / stdHeight
  if(newRat > aspRat):
    resizeWidth = stdWidth
    resizeHeight = round(resizeWidth * aspRat)
  else:
    resizeHeight = stdHeight
    resizeWidth = round(resizeHeight / aspRat)
  nextImg = nextImg.resize((resizeWidth, resizeHeight))
  nextPI = PIL.ImageTk.PhotoImage(nextImg)
  imageLabel.configure(image=nextPI)
  imageLabel.image = nextPI

def prev():
  global current, stdHeight, stdWidth
  # update the picture index value
  if(current > 0):
    current -= 1
    updateIndex = str(current + 1) + "/" + str(len(allPicts))
    pictIndex.config(text=updateIndex)
    title.config(text=allPicts[current])
    #print("current index: " + updateIndex)

  # update the current display
  prevImg = PIL.Image.open(allPicts[current])
  ogWidth, ogHeight = currImg.size
  aspRat = ogWidth / ogHeight
  newRat = stdWidth / stdHeight
  if(newRat > aspRat):
    resizeWidth = stdWidth
    resizeHeight = round(resizeWidth * aspRat)
  else:
    resizeHeight = stdHeight
    resizeWidth = round(resizeHeight / aspRat)
  prevImg = prevImg.resize((resizeWidth, resizeHeight))
  prevPI = PIL.ImageTk.PhotoImage(prevImg)
  imageLabel.configure(image=prevPI)
  imageLabel.image = prevPI

Label(frame, text='new name ').pack(side=LEFT)        # label for the new name textbox/ entry
nameEntry = Entry(frame, textvariable=nameVar)        # make the textbox/ entry
nameEntry.pack(side=LEFT)
prevBtn = tk.Button(bottomframe, text='< prev ', fg='blue', command=prev)
prevBtn.pack(side=LEFT)
submitBtn = tk.Button(frame, text='Submit', fg='green', command=submit)  # make the save button
submitBtn.pack(side=LEFT)
pictIndex = Label(bottomframe, text=indexStr)         # put the picture index in a label widget
pictIndex.pack(side=LEFT)
nextBtn = tk.Button(bottomframe, text=' next >', fg='blue', command=next)
nextBtn.pack(side=LEFT)
root.mainloop()               # an infinite loop that runs as long as the main window isn't closed