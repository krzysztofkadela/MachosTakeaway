from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation # import Reservation modal to display reservations.

@login_required  # Ensures the user is logged in
def make_reservationold(request):
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

@login_required  # Ensures the user is logged in
def make_reservation(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
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

    return render(request, 'reservation/make_reservation.html', {
        'form': form,
        'reservations': reservations  # Pass the reservations to the template
    })