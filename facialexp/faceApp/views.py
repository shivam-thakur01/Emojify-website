from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt
import cv2
import base64

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# def index(request):
#     return render(request,'index.html',context={'status':200,'prediction':None})

def picClick(request):
    return render(request,'picClick.html')

def videoClick(request):
    return render(request,'videoClick.html')

@api_view(['post'])
def modelPredict(request):
    imageurl=request.data['s'][22:]
    # print(imageurl)
    label=imageClassifier(imageurl)
    print(label)
    return Response({'status':200,'prediction':label})
    # return render(request,'index.html',context={'status':200,'prediction':label})
    
def imageClassifier(imgurl):
    label=None
    images = imgurl
    decoded_data = base64.b64decode(images)
    img = imread(io.BytesIO(decoded_data))
    cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    face_classifier = cv2.CascadeClassifier(
        r"C:\Users\satya\OneDrive\Documents\web-dev\Facial expression Recog web\haarcascade_frontalface_default.xml")
    classifier = load_model(
        r"C:\Users\satya\OneDrive\Documents\web-dev\Facial expression Recog web\classifier_model.h5")

    class_labels = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']

    frame = cv2_img
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(frame, 1.3, 5)
    # print(faces, gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        if np.sum([roi_gray]) != 0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = classifier.predict(roi)[0]
            label = class_labels[preds.argmax()]
            # print(label)
    return label
