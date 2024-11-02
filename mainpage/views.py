from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html') # Render main page index.html.