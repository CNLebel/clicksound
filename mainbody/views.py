from django.shortcuts import render
from mainbody.models import *

# Create your views here.

def index(request):

    #photolbum make data start
    photolbumone = IndexPhotoLbum.objects.filter(imgnumber=1)
    photolbumtwo = IndexPhotoLbum.objects.filter(imgnumber=2)
    photolbumthree = IndexPhotoLbum.objects.filter(imgnumber=3)
    photolbumfour = IndexPhotoLbum.objects.filter(imgnumber=4)

    article=IndexArticle.objects.all()

    centext={
        #photolbum start
        'photolbumone':photolbumone,
        'photolbumtwo':photolbumtwo,
        'photolbumthree':photolbumthree,
        'photolbumfour':photolbumfour,
        #article start
        'article':article,

    }
    return render(request,'mainbody/index.html',centext)

def about(request):
    #bottompicture make data start
    bottompicture=AboutBottomPicture.objects.all()

    centext={
        #bottompicture start
        'bottompicture':bottompicture,
    }
    return render(request,'mainbody/about.html',centext)

def tweets(request):
    return render(request,'mainbody/tweets.html')

def writings(request):
    return render(request,'mainbody/writings.html')