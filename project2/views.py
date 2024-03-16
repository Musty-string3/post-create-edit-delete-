from django.shortcuts import render, redirect, reverse
from django.views import View

def index(request):
    return redirect('sample_app:create_post')