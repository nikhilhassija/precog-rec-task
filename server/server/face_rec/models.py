from django.db import models
from django.core.files import File

import os

class TrainImage(models.Model):
	image = models.ImageField(upload_to="train/")

	label = models.ForeignKey("Label")

	def __str__(self):
		return self.label.name

class Label(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

class TestImage(models.Model):
	orig_img = models.ImageField(upload_to="test/", null=True)
	face_img = models.ImageField(upload_to="test/", null=True)

	has_face = models.BooleanField(default=False)
	has_modi = models.BooleanField(default=False)
	has_kejr = models.BooleanField(default=False)
