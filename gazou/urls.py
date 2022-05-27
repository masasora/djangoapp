from django.urls import path
from . import views
from . import twitter_follower

urlpatterns = [
    path('', views.index, name='index'),
    path('gazougazou',twitter_follower.twifow,name='gazougazou'), 
]
