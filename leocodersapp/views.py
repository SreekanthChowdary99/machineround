from leocodersapp.models import Schedule
from leocodersapp.serializers import ScheduleSerializer,UserSerializer
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import User,OutCsv
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import ScheduleForm
from .serializers import ScheduleSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

User = get_user_model()

# this viewset is used for viewing and creating schedules using django rest framework 
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

#this view is used for the user signup using django rest framework
class SignupViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#this view shows and creates the schedules
def home_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ScheduleForm(request.POST)
            if form.is_valid():
                data=request.POST
                date=data.get("date")
                timeslot=data.get("timeslot")
                name=data.get("name")
                user_id=request.user.id
                Schedule.objects.create(date=date,timeslot=timeslot,name=name,user_id=user_id)
                return redirect('/')
        else:
            form = ScheduleForm()
            schedules=Schedule.objects.filter(user_id=request.user.id)
            print(schedules)
        return render(request, 'registration/home.html', {'form': form,'schedules':schedules})
    else:
        print("unauthorised")

# this view is used for the user to register
def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# this view is used for login
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form, 'title':'log in'})