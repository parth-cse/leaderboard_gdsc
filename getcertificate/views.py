from django.shortcuts import render

# Create your views her
def get(request):
    return render(request, 'getcertificate/comingsoon.html')

