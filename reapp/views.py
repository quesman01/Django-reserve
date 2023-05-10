# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation has been made successfully!')
            return redirect('success')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})

