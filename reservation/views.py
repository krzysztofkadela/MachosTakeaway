from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been made successfully!')
            return redirect('index')  # Redirect to an appropriate after-save page
    else:
        form = ReservationForm()
    
    return render(request, 'reservation/make_reservation.html', {'form': form})