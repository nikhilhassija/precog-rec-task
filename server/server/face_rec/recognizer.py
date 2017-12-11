import cv2
import numpy as np

import os

from server.settings import BASE_DIR

from .models import TrainImage, Label

lbph_rec = cv2.face.LBPHFaceRecognizer_create()

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

def train():
	print("======= Recognizer Training =======")

	global lbph_rec

	faces = []
	label = []

	for train_img in TrainImage.objects.all():
		img = cv2.imread(train_img.image.path)
		lab = train_img.label.id

		faces.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
		label.append(lab)

	label = np.asarray(label)

	lbph_rec.train(faces, label)

	print("======= Recognizer Trained =======")
	

def get_faces(image):
	face_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR, "haarcascades/haarcascade_frontalface_default.xml"))
	faces = face_cascade.detectMultiScale(image)

	for face in faces:
		yield face

def face_rec(filepath):
	img = cv2.imread(filepath)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	labels = []
	confs = []

	global lbph_rec

	for x, y, w, h in get_faces(img):
		label, conf = lbph_rec.predict(img[y:y+w, x:x+h])

		labels.append(label)
		confs.append(conf)

	return labels, confs 

train()