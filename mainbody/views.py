from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainbody/index.html')

def about(request):
    return render(request,'mainbody/about.html')

def tweets(request):
    return render(request,'mainbody/tweets.html')