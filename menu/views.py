from django.shortcuts import render, redirect

# Create your views here.

def menu(request):
    return render(request, 'menu/menu.html')

def redirect_menu_html(request):
    return redirect('menu')  # Redirect to the 'menu' named URL