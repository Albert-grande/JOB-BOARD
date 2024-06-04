from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from . models import Job, Userprofile

# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, 'Jobhub/index.html', {'jobs':jobs})

def auth(request):
    return render(request, 'Jobhub/auth.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                account_type = request.POST.get('account_type', 'jobseeker')
                
                if account_type == 'employer':
                    userprofile = Userprofile.objects.create(user=user, is_employer=True)
                    userprofile.save()
                else:
                    userprofile = Userprofile.objects.create(user=user)
                    userprofile.save()

                messages.success(request, 'Successfully registered😊, Please Login to ⨈erify your infomation ⨀')
                return redirect('auth')
        else:
            messages.error(request, 'Passwords do not match')

    return redirect('auth')
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'ThankYou For choosing Grande Job Hub')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return redirect('auth')


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'Jobhub/job_detail.html', {'job':job})

@login_required
def dasboard(request):
    return render(request, 'Jobhub/dashboard.html', {'userprofile':request.user.userprofile})

def dash_home(request):
    return render(request, 'Jobhub/dash_home.html',{'userprofile':request.user.userprofile})