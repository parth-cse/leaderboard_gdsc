from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from student.models import *

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def all(request):

    if 'searchbar' in request.GET:
        r = request.GET['searchbar']

        data = Student.objects.filter(name__icontain=r)
    else:
        data = Student.objects.all()
    contexts = {'student': data }

    context = contexts

    return render(request, 'home/all.html', context)


def gold(request):
    contexts = {'student': Student.objects.all()}

    context = contexts

    return render(request, 'home/gold.html', context)

def silver(request):
    contexts = {'student': Student.objects.all()}

    context = contexts

    return render(request, 'home/silver.html', context)

def bronze(request):
    contexts = {'student': Student.objects.all()}

    context = contexts

    return render(request, 'home/bronze.html', context)

def runner(request):
    contexts = {'student': Student.objects.all()}

    context = contexts

    return render(request, 'home/runner.html', context)

def genai(request):
    contexts = {'student': Student.objects.all()}

    context = contexts

    return render(request, 'home/genai.html', context)

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = Student.objects.filter(email = email)

        if not user_obj.exists():
            messages.warning(request, 'Please Enter Valid Email Linked to your CloudSkill Boost')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        if user_obj:
            if user_obj.rank <= 80:
                user_obj.sized_entered = True

        # Save the updated user object
                user_obj.save()

        # Redirect to the desired page
                return redirect('https://docs.google.com/forms/d/e/1FAIpQLSeMk4SyvWx44fx2EeZuzZbcyqDvGdamMyWorFKfgghks7djpw/viewform?usp=sf_link')
            else:
                messages.error(request, "Please try After Sometime")
                return HttpResponseRedirect(request.path_info)
    
    return render(request ,'accounts/login.html')

