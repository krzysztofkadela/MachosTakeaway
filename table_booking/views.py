from django.shortcuts import render, redirect
from .models import Table, TableBooking
from .forms import TableBookingForm
from django.contrib.auth.decorators import login_required

@login_required  # Protect this view
def book_table(request):
    if request.method == 'POST':
        form = TableBookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()  # Save the instance after validating
            table = booking.table
            table.is_booked = True  # Mark the selected table as booked
            table.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        # Get the number of people from the form (this will be in the form's data)
        num_people = request.GET.get('num_people', 1)  # Default to 1 if nothing is selected
        # Get available tables based on the number of people
        available_tables = Table.objects.filter(is_booked=False).filter(size__gte=num_people)  # Tables that can accommodate at least the chosen number of people
        
        form = TableBookingForm(user=request.user)  # Initialize clean form
    return render(request, 'table_booking/book_table.html', {'form': form, 'tables': available_tables})