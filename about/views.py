from django.shortcuts import render, redirect
from .models import About

# Create your views here.

# View to display about information
def about_view(request):
    abouts = About.objects.all()  # Fetch all About objects
    return render(request, 'about/about.html', {'abouts': abouts})

# View to simply render the about page (if needed)
def about(request):
    return render(request, 'about/about.html')

# Redirect view to the about page
def redirect_about_html(request):
    return redirect('about')  # Redirect to the 'about' named URL