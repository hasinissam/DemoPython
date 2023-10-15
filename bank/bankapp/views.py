# views.py inside your app
from django.shortcuts import render
def home(request):
    return render(request,'home.html')

