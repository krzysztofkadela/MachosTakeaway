from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)  # Do not save to DB yet
            reservation.user = request.user  # Associate the logged-in user
            reservation.save()  # Now save the reservation
            messages.success(request, 'Your reservation has been made successfully!')
            return redirect('index')  # Redirect to an appropriate page after saving
    else:
        form = ReservationForm()

    return render(request, 'reservation/make_reservation.html', {'form': form})