from django.shortcuts import render

def home(request):
    return render(request, 'lookup/home.html')