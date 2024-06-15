from rest_framework import viewsets
from .models import Booking, Room, Availabity
from .serializers import BookingSerializer, RoomSerializer, AvailabilitySerializer
from django.shortcuts import render, redirect
from django.views import View
from .forms import BookingForm



class BookingFormView(View):
    def get(self, request):
        form = BookingForm
        return render(request, 'booking/booking_form.html', {'form': form})
    
    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_form')
        return render(request, 'booking/booking_form.html', {'form': form})
    



class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer




class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer




class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer    