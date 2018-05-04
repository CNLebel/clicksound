from django.conf.urls import include, url
from mainbody import views

urlpatterns = [
    url('^index',views.index,name='index'),
    url('^$',views.index,name='index'),
    url('^about',views.about,name='about'),
    url('^tweets',views.tweets,name='tweets'),
    url('^writings',views.writings,name='writings'),
]
