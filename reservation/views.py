from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Reservation # import Reservation modal to display reservations.
from datetime import datetime, timedelta


@login_required  # Ensures the user is logged in
def make_reservationold(request):
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

@login_required  # Ensures the user is logged in
def make_reservation(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-booking_date', '-booking_time')
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Extract the booking_date and booking_time from cleaned data
            booking_date = form.cleaned_data['booking_date']
            booking_time_str = form.cleaned_data['booking_time']  # This is a string
            
             # Convert booking_time_str from string to time
            booking_time = datetime.strptime(booking_time_str, "%H:%M").time()  # Converts string to time
            
            booking_datetime = datetime.combine(booking_date, booking_time)
            current_datetime_plus_24h = datetime.now() + timedelta(hours=24)

            # Validate that the booking date is at least 24 hours in advance
            if booking_datetime < current_datetime_plus_24h:
                messages.warning(request, "Warning: Reservations must be made at least 24 hours in advance.")
            else:
                # The form has passed validation; we can save the reservation
                reservation = form.save(commit=False)  # Do not save to DB yet
                reservation.user = request.user  # Associate the logged-in user
                reservation.save()  # Now save the reservation
                messages.success(request, 'Your reservation has been made successfully!')
                return redirect('index')  # Redirect to an appropriate page after saving
        else:
            # If the form is invalid, get the first validation error for display
            messages.error(request, "There was an error with your reservation. Please check your input.")
    else:
        form = ReservationForm()

    return render(request, 'reservation/make_reservation.html', {
        'form': form,
        'reservations': reservations  # Pass the reservations to the template
    })

@login_required
def cancel_reservation(requst, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, user=requst.user) # Get reservation for user request
        reservation.delete() # delete reservation
        messages.success(requst, 'Reservation has been cancelled successfully!')
    except Reservation.DoesNotExist:
        messages.error(requst, 'Reservation not found or you do not have permission to cancel it.')

    return redirect('make_reservation') #redirect back to the reservation form page.  

