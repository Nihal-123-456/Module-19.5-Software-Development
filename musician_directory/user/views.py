from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .import models
from .import forms


# Create your views here.
class signup_form(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('signup')  
    template_name = 'signup.html'

    def form_valid(self, form):
        messages.success(self.request, 'Signup Successful')
        response = super().form_valid(form)
        return response

class login_form(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Log in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Incorrect information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@method_decorator(login_required, name='dispatch')
class addmusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class addalbum(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class editmusician(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class editalbum(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class deletealbum(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class albumlist(View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        albums = models.Album.objects.all()
        context = {'albums': albums}
        return render(request, self.template_name, context)