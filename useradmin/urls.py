from django.conf.urls import include, url
from useradmin import views


urlpatterns = [
    # url('^login',views.login,name='login'),
    url('^register',views.register, name='register'),
]
