from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',albumlist.as_view(), name='home'),
    path('signup/',signup_form.as_view(), name='signup'),
    path('login/',login_form.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('add/album', addalbum.as_view(), name='add_album'),
    path('edit_album/<int:id>/', editalbum.as_view(), name='edit_album'),
    path('delete/<int:id>', deletealbum.as_view(), name='delete_album'),
    path('add/musician', addmusician.as_view(), name='add_musician'),
    path('edit_musician/<int:id>/', editmusician.as_view(), name='edit_musician'),
]