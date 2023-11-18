from django.urls import path
from home.views import *

urlpatterns = [
   
    path('' , index , name="index"),
    path('Leaderboard', all, name="all"),
    path('Leaderboard/gold', gold, name="gold"),
    path('Leaderboard/silver', silver, name="silver"),
    path('Leaderboard/bronze', bronze, name="bronze"),
    
    path('Leaderboard/runnerup', runner, name="runner"),
    
    path('Leaderboard/genai', genai, name="genai"),
    path('activate/', login_page, name='tick')
    
]
