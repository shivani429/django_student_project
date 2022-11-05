from dataclasses import fields
from django import forms
from demoapp.models import *

class StudentForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    roll_no = forms.IntegerField(label='Roll no')
    class_no = forms.IntegerField(label='class no')
    address = forms.CharField(label='Address', max_length=70)
 
