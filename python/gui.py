#!/usr/bin/env python
# by duo Dec 2017

import cv2
import time
import numpy as np
import os
import argparse
from datetime import datetime
import shutil

def show_webcam(mirror=False, numCam=-1):
  global img, txt
  txt = ' '
  frequency = 100 # Hertz
  duration  = 50 # milliseconds
  cam = cv2.VideoCapture(numCam)
  time.sleep(0.5)
  start_time = time.time()
  cv2.namedWindow('Amanajé', cv2.WINDOW_NORMAL)
  while True:
    ret_val, img = cam.read()
    if mirror: 
      img = cv2.flip(img, 1)
    height, width = img.shape[1::-1]
    cv2.setMouseCallback('Amanajé', onMouse)
    cv2.putText(img, txt, (int(width*0.5), int(height*0.05)), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Amanajé', img)
    elapsed_time = time.time() - start_time
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) & 0xFF == 27:
      break  # esc to quit
  cv2.destroyAllWindows()

def onMouse(event, x, y, flags, param):
  # grab references to the global variables
  global refPt, cropping, img, txt
  cropping = False
  # if the left mouse button was clicked, record the starting
  # (x, y) coordinates and indicate that cropping is being
  # performed
  if event == cv2.EVENT_LBUTTONDOWN:
    refPt = [(x, y)]
    cropping = True
 
  # check to see if the left mouse button was released
  elif event == cv2.EVENT_LBUTTONUP:
    # record the ending (x, y) coordinates and indicate that
    # the cropping operation is finished
    refPt.append((x, y))
    cropping = False
 
  # draw a rectangle around the region of interest
  #cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
  txt = 'Mouse : (' + str(x) + ', ' + str(y) + ')'
  if cropping:
    txt += ' cropping'
  else:
    txt += ' not cropping'

def main():
  show_webcam(mirror=False, numCam=0)


main()
