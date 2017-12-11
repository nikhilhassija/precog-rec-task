import numpy as np 
import cv2 

import sys

face_cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")

name = sys.argv[1]

img = cv2.imread("./{}".format(name))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x, y, w, h = face_cascade.detectMultiScale(gray)[0]

img = img[y:y+h, x:x+w]

cv2.imwrite("./faces/{}".format(name), img)