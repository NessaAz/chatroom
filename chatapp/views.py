from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from .forms import *


# rooms =[
#     {'id':1, 'name': 'intro to data structures'},
#     {'id':2, 'name': 'intro to data algorithms'},
#     {'id':3, 'name': 'full stack development'},

# ]

def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) #creates a session in the browser
            return redirect('home')
        else:
            messages.error(request, 'username or password does not exist')

    context = {}
    return render(request, 'chatapp/register_login.html', context)



def logout_user(request):
    logout(request)
    return redirect('home')



def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
    Q(name__icontains=q)|
    Q(description__icontains=q)    
    )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count}
    return render(request, 'chatapp/home.html', context)




def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'chatapp/room.html', context)



@login_required(login_url='login')
def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context={'form':form}
    return render(request, 'chatapp/room_form.html', context)



@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You need to login first!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'chatapp/room_form.html', context)




@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You need to login first!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'chatapp/delete.html', {'obj':room})




