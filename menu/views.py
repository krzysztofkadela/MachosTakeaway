from django.shortcuts import render, redirect
from .models import MenuItem  # Importing MenuItem model

# Create your views here.


def menu(request):
    menu_items = MenuItem.objects.all()  # Retrieve all MenuItem objects
    return render(request, 'menu/menu.html', {'menu_items': menu_items})


def redirect_menu_html(request):
    return redirect('menu')  # Redirect to the 'menu' named URL
