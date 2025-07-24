from bookings.models import EquipmentBooking
from rest_framework import serializers


class EquipmentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentBooking
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
