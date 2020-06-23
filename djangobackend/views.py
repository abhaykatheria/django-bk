from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import settings
import os
import cv2
import numpy as np
from PIL import Image
import base64
import matplotlib.pyplot as plt
from PIL import Image
from base64 import decodestring

from .imgseg import Segmentation



def home(request):
    return render(request, 'home.html')

@csrf_exempt
@csrf_exempt
def image_seg(request):
    if request.method == 'POST':
        
        x = request.body
        print(x[:34])
        head = x[:32]
        x=x[32:-2]
        t = base64.b64decode(x)
        f = open(settings.MEDIA_ROOT + '/someimage.jpg', 'wb')
        f.write(t)
        f.close()

        nparr = np.fromstring(t, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        IS=Segmentation(img,2)
        new_img = IS.draw_image()
        fig,ax = plt.subplots()
        ax.axis("off")
        ax.set_title("No. of colors : "+"2")
        ax.imshow(new_img)
        ax.figure.savefig(settings.MEDIA_ROOT + '/output.jpg')
        fig.canvas.draw()

        f = open(settings.MEDIA_ROOT + '/output.jpg', 'rb')
        op = f.read()
        op = base64.b64encode(op)

        return HttpResponse(head[9:]+op)

@csrf_exempt
@csrf_exempt

def thug(request):
    if request.method == 'POST':
        
        x = request.body
        print(x[:34])
        head = x[:32]
        x=x[32:-2]
        t = base64.b64decode(x)
        f = open(settings.MEDIA_ROOT + '/someimage.jpg', 'wb')
        f.write(t)
        f.close()

        img=cv2.imread(settings.MEDIA_ROOT + '/someimage.jpg')
        thug = Image.open(settings.MEDIA_ROOT + '/mask.png' )
        face_cascade = cv2.CascadeClassifier(settings.MEDIA_ROOT + "/haarcascade_frontalface_alt.xml")
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray,1.3,5)
        bkg = Image.fromarray(img)
        for (x,y,w,h) in face:
            new_thug = thug.resize((w,h) , Image.ANTIALIAS)
            bkg.paste(new_thug , (x,y), mask = new_thug)
        cv2.imwrite(settings.MEDIA_ROOT +'/output.jpg',np.asarray(bkg))

        f = open(settings.MEDIA_ROOT + '/output.jpg', 'rb')
        op = f.read()
        op = base64.b64encode(op)

        return HttpResponse(head[9:]+op)
