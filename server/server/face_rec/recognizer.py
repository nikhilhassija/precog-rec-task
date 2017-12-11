import cv2
import numpy as np

import os

from server.settings import BASE_DIR

def face_detect(filename, filedir):
	filepath = os.path.join(filedir, filename)

	face_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR, "haarcascades/haarcascade_frontalface_default.xml"))

	img  = cv2.imread(filepath)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray)

	for x, y, w, h in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)

	face_name = "face_" + filename
	face_path = os.path.join("/tmp", face_name)

	cv2.imwrite(face_path, img)

	return face_path, bool(len(faces))