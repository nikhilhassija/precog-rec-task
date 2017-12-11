from django.contrib import admin

from .models import Label, TrainImage, TestImage

admin.site.register(Label)
admin.site.register(TrainImage)
admin.site.register(TestImage)