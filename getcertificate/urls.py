from django.urls import path
from getcertificate.views import *

urlpatterns = [
    path('getcertificate/', get, name='get')
    ]
