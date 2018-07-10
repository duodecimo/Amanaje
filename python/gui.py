#!/usr/bin/env python
# by duo Dec 2017

import tkinter
import cv2
import time
import numpy as np
import os
import argparse
from datetime import datetime
import shutil
from PIL import Image, ImageTk

global drawing

width, height = 800, 600
cam = cv2.VideoCapture(-1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window = tkinter.Tk()
window.title('Amanajé')
window.bind('<Escape>', lambda e: window.quit())

canvas = tkinter.Label(window)
canvas.pack()
drawing = False
txt = ' '

def show_webcam():
  global drawing
  _, frame = cam.read()
  frame = cv2.flip(frame, 1)
  x = window.winfo_pointerx() - window.winfo_rootx()
  y = window.winfo_pointery() - window.winfo_rooty()
  txt = 'Mouse : (' + str(x) + ', ' + str(y) + ')'
  if drawing:
    txt += ' drawing'
  cv2.putText(frame, txt, (int(width*0.3), int(height*0.05)), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)
  cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
  img = Image.fromarray(cv2image)
  imgtk = ImageTk.PhotoImage(image=img)
  canvas.imgtk = imgtk
  canvas.configure(image=imgtk)
  canvas.after(10, show_webcam)

def toggleDraw():
  global drawing
  drawing = not drawing

btn_snapshot=tkinter.Button(window, text="Draw", width=50, command=toggleDraw)
btn_snapshot.pack(anchor=tkinter.CENTER, expand=False)

show_webcam()
window.mainloop()

