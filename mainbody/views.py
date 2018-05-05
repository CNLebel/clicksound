from django.shortcuts import render
from mainbody.models import *
from django.core.paginator import *

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

    #vitae make data start
    vitae=AboutVitae.objects.all()

    centext={
        #bottompicture start
        'bottompicture':bottompicture,
        #vitae start
        'vitae':vitae,
    }
    return render(request,'mainbody/about.html',centext)

def tweets(request,pindex):
    #essay make data start
    list=TweetsEssay.objects.all()
    paginator = Paginator(list, 5)
    essay=paginator.page(int(pindex))


    centext={
        #essay start
        'essay':essay,
    }
    return render(request,'mainbody/tweets.html',centext)

def writings(request):
    return render(request,'mainbody/writings.html')