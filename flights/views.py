from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer
import datetime


class FlightList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightListSerializer


class BookingsList(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.datetime.today())
    serializer_class = BookingListSerializer
