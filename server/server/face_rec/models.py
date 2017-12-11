from django.db import models
from django.core.files import File

import os

import face_rec.recognizer as recognizer

class TrainImage(models.Model):
	image = models.ImageField(upload_to="train/")

	label = models.ForeignKey("Label")

class Label(models.Model):
	name = models.CharField(max_length = 100)

class TestImage(models.Model):
	orig_img = models.ImageField(upload_to="test/", null=True)
	face_img = models.ImageField(upload_to="test/", null=True)

	has_face = models.BooleanField(default=False)
	has_modi = models.BooleanField(default=False)
	has_kejr = models.BooleanField(default=False)

	def do_face_detect(self):
		basedir = os.path.dirname(self.orig_img.path)
		basename = os.path.basename(self.orig_img.path)

		face_path, faces = recognizer.face_detect(basename, basedir)

		self.has_face = faces
		self.face_img = File(open(face_path, "rb"))

		self.save()