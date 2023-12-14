from django import forms
from .models import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import *

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = '__all__'
        rating_choice = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
        widgets = {
            'rating': forms.RadioSelect(choices=rating_choice),
            'release_date' : forms.NumberInput(attrs={'type': 'date'})
        }

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')