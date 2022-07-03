import tkinter as tk
from tkinter import *
from tkinter import filedialog 
from tkinter import simpledialog
import os
import numpy as np
import imageio
import scipy.ndimage
import cv2

win = Tk()
win.geometry("400x400")
win.title("Image to sketch")

def browse():
    global img
    filename = filedialog.askopenfilename(title = "Select a File")
    img = (filename)

def sketch():
    global img
    def grayscale(rgb):
        return np.dot(rgb[...,:3],[0.299,0.587,0.114])

    def dodge(front,back):
        result=front*250/(250-back)
        result[result>255]=250
        result[back==255]=250
        return result.astype('uint8')

    s=imageio.imread(img)
    g=grayscale(s)
    i=255-g

    b=scipy.ndimage.filters.gaussian_filter(i,sigma=75)
    r=dodge(b,g)
    f = Tk()
    f.withdraw()
    name= simpledialog.askstring(title="Save as", prompt="enter name of image")
    filepath= filedialog.askdirectory(parent=f,initialdir="/",title='Please select a folder')
    t= name +'.png'
    cv2.imwrite(os.path.join(filepath,t),r)
    f.mainloop()


Label_1 = Label(win, text="Browse A File", width=20, font=("bold", 15))
Label_1.place(x=80, y=10)
Label_2 = Label(win, text="Created By ", width=80, font=("bold", 8))
Label_2.place(x=-48, y=250)
Label_3 = Label(win, text="Rushabh Dhamne ", width=80, font=("bold", 8))
Label_3.place(x=-48, y=275)
Label_4 = Label(win, text="Omkar Chavan ", width=80, font=("bold", 8))
Label_4.place(x=-48, y=290)
Label_5 = Label(win, text="Akash Chaudhari ", width=80, font=("bold", 8))
Label_5.place(x=-48, y=305)

Button(win,text='Browse an Image',command=browse, width=20, height=2, bg="blue", fg="white").place(x=120,y=50)
Button(win,text='Image to sketch',command=sketch, width=20, height=2, bg="blue", fg="white").place(x=120,y=100)

win.mainloop()
