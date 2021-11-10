from django.conf.urls import url
from django.urls import path
 
from .views import user_login, register
 
urlpatterns = [
    path('signup/', register, name='signup'),
    url(r'^login/$', user_login, name='login'), 

]