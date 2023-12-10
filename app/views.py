from django.shortcuts import render

# Create your views here.

def downloaded(request):
    return render(request,'downloaded.html')
