from multiprocessing import context
from django.shortcuts import render

rooms =[
    {'id':1, 'name': 'intro to data structures'},
    {'id':2, 'name': 'intro to data algorithms'},
    {'id':3, 'name': 'full stack development'},

]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')

