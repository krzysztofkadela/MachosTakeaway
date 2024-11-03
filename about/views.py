from django.shortcuts import render, redirect

# Create your views here.

def about(request):
    return render(request, 'about/about.html')

def redirect_about_html(request):
    return redirect('about')  # Redirect to the 'about' named URL