from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# rooms =[
#     {'id':1, 'name': 'intro to data structures'},
#     {'id':2, 'name': 'intro to data algorithms'},
#     {'id':3, 'name': 'full stack development'},

# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'chatapp/home.html', context)

def room(request, pk):
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'chatapp/room.html', context)

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


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'chatapp/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'chatapp/delete.html', {'obj':room})