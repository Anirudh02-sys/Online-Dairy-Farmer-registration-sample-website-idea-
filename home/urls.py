from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # if the path is blank run the index function in views.py
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("certification", views.certification, name='certification'),
    path("certifiedlist", views.certifiedlist, name='certifiedlist'),
    path("contact", views.contact, name='contact'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("join", views.join, name='join'),
    path("certform1", views.certform1, name="certform1"),
    path("certform3", views.certform3, name="certform3"),
    path("certform2", views.certform2, name="certform2"),
    

]
