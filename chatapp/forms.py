from dataclasses import fields
from xml.parsers.expat import model
from django.forms import ModelForm
from .models import *

class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields = '__all__'