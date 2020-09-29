from django.shortcuts import render, redirect
from product.models import Images
from opencv_app.forms import ImageForm, ImageEditForm
import cv2
import numpy as np
from matplotlib import pyplot as plt
# Create your views here.

def IndexView(request):
    images = Images.objects.all().order_by("-id")
    context = {
        "images": images
    }
    return render(request, 'indexcv.html', context)


def EditCv2ImageView(request, id):
    form = ImageEditForm(request.POST or None, request.FILES or None)
    image = Images.objects.get(id=id)

    if form.is_valid():
        image = Images.objects.get(id=id)

        # opencv start
        img_main = cv2.imread(image.image.path, cv2.IMREAD_GRAYSCALE)
        thresh = form.cleaned_data['thresh']

        candidate_img = cv2.threshold(img_main, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(image.modified_image.path, candidate_img)
        # opencv end

        imagess = Images.objects.all().order_by("-id")
        context = {
            "images": imagess
        }

        return render(request, 'indexcv.html', context)

    context = {
        "form": form,
        "image": image
    }
    return render(request, "imageedit.html", context)


def edit(request, id):
    form = ImageEditForm(request.POST or None, request.FILES or None)
    image = Images.objects.get(id=id)

    if form.is_valid():
        image = Images.objects.get(id=id)

        img_main = cv2.imread(image.image.path, cv2.IMREAD_GRAYSCALE)
        thresh = form.cleaned_data['thresh']

        candidate_img = cv2.threshold(img_main, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(image.modified_image.path, candidate_img)

        return redirect("IndexView")

    context = {
        "form": form,
        "image": image
    }
    return render(request,"imageedit.html",context)
