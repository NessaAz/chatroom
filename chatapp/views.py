from multiprocessing import context
from django.shortcuts import render

rooms =[
    {'id':1, 'name': 'intro to data structures'},
    {'id':2, 'name': 'intro to data algorithms'},
    {'id':3, 'name': 'full stack development'},

]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'chatapp/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
   
    context = {'room':room}
    return render(request, 'chatapp/room.html', context)

