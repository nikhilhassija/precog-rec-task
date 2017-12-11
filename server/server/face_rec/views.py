from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import TestImage

def index(request):
	if request.method == "POST" and request.FILES["image"]:
		test_img = TestImage()
		test_img.orig_img = request.FILES["image"] 		

		test_img.save()

		test_img.do_face_detect()

		return render(request, "result.html", {"image": test_img})


	return render(request, "index.html", {})