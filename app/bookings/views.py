from bookings.models import EquipmentBooking
from rest_framework import generics, permissions
from bookings.utils import EquipmentBookingFilter
from django_filters import rest_framework as filters
from bookings.serializers import EquipmentBookingSerializer


class BookingList(generics.ListCreateAPIView):
    queryset = EquipmentBooking.objects.all()
    serializer_class = EquipmentBookingSerializer


class UserBookingList(generics.ListAPIView):
    queryset = EquipmentBooking.objects.all()
    serializer_class = EquipmentBookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EquipmentBookingFilter

    def get_queryset(self):
        user = self.request.user
        return EquipmentBooking.objects.filter(user=user)


class ManageUserBooking(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentBooking.objects.all()
    serializer_class = EquipmentBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return EquipmentBooking.objects.filter(user=self.request.user)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentBooking.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipmentBookingSerializer
