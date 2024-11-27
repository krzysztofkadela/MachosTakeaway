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
            booking.user = request.user  # Assign the user if not done in the form
            booking.save()
            table = booking.table
            table.is_booked = True  # Mark the selected table as booked
            table.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        # Get the number of people to filter available tables
        num_people = request.GET.get('num_people', 1)

        # Convert to an integer and filter available tables based on selection
        try:
            num_people = int(num_people)
        except ValueError:
            num_people = 1

        # Get available tables based on the number of people selected
        available_tables = Table.objects.filter(is_booked=False, size__gte=num_people)

        # Initialize clean form
        form = TableBookingForm(user=request.user)

        # Create a list of numbers from 1 to 6
        number_choices = list(range(1, 7))

    return render(request, 'table_booking/book_table.html', {'form': form, 'tables': available_tables, 'number_choices': number_choices})