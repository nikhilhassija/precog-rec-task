from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files import File

from .models import TestImage
import face_rec.recognizer as recognizer


import os

def index(request):
	if request.method == "POST" and request.FILES["image"]:
		test_img = TestImage()
		test_img.orig_img = request.FILES["image"] 		

		test_img.save()

		has_face = do_face_detect(test_img)

		if has_face:
			do_face_rec(test_img)

		return render(request, "result.html", {"image": test_img})


	return render(request, "index.html", {})


def do_face_detect(test_img):
	basedir = os.path.dirname(test_img.orig_img.path)
	basename = os.path.basename(test_img.orig_img.path)

	face_path, faces = recognizer.face_detect(basename, basedir)

	test_img.has_face = faces
	test_img.face_img = File(open(face_path, "rb"))

	test_img.save()

	return faces

# Modi == 1
# Kejr == 2
def do_face_rec(test_img):
	labels, confs = recognizer.face_rec(test_img.orig_img.path)

	for label, conf in zip(labels, confs):
		if conf < 100:
			if label == 1:
				test_img.has_modi = True

			if label == 2:
				test_img.has_kejr = True

	test_img.save()

	pass