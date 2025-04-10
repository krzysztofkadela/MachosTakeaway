from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

from .forms import ReservationForm
from .models import Reservation


@login_required
def make_reservation(request):
    """
    View to allow logged-in users to make reservations.
    Validates that bookings are made at least 24 hours in advance.
    """
    reservations = Reservation.objects.filter(
        user=request.user
    ).order_by('-booking_date', '-booking_time')

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            booking_time_str = form.cleaned_data['booking_time']
            booking_time = datetime.strptime(
                booking_time_str, "%H:%M"
            ).time()
            booking_datetime = datetime.combine(booking_date, booking_time)

            if booking_datetime < datetime.now() + timedelta(hours=24):
                messages.warning(
                    request,
                    "Warning: Reservations must be made at least 24 hours "
                    "in advance."
                )
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(
                    request,
                    'Your reservation has been made successfully!'
                )
                return redirect('index')
        else:
            messages.error(
                request,
                "There was an error with your reservation. "
                "Please check your input."
            )
    else:
        form = ReservationForm()

    return render(request, 'reservation/make_reservation.html', {
        'form': form,
        'reservations': reservations
    })


@login_required
def cancel_reservation(request, reservation_id):
    """
    View to allow users to cancel their own reservations.
    """
    try:
        reservation = Reservation.objects.get(
            id=reservation_id,
            user=request.user
        )
        reservation.delete()
        messages.success(
            request,
            'Reservation has been cancelled successfully!'
        )
    except Reservation.DoesNotExist:
        messages.error(
            request,
            'Reservation not found or you do not have permission to cancel it.'
        )

    return redirect('make_reservation')
