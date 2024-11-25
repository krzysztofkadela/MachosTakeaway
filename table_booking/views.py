from django.shortcuts import render, redirect
from .models import Table, TableBooking
from .forms import TableBookingForm
from django.contrib.auth.decorators import login_required

@login_required  # Protect this view to ensure only logged in users can access it
def book_table(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the currently authenticated user
            booking.save()
            table = booking.table
            table.is_booked = True  # Mark table as booked
            table.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        tables = Table.objects.filter(is_booked=False)  # Get available tables
        form = TableBookingForm()  # Initialize clean form
    return render(request, 'table_booking/book_table.html', {'form': form, 'tables': tables})