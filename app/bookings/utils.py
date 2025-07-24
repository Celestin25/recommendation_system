from django.utils import timezone
from bookings.models import EquipmentBooking
from django_filters import rest_framework as filters


class EquipmentBookingFilter(filters.FilterSet):
    past_bookings = filters.BooleanFilter(method='filter_past_bookings')
    upcoming_bookings = filters.BooleanFilter(method='filter_upcoming_bookings')

    class Meta:
        model = EquipmentBooking
        fields = ['past_bookings', 'upcoming_bookings']

    def filter_past_bookings(self, queryset, name, value):
        if value:
            return queryset.filter(end_date__lt=timezone.now())
        return queryset

    def filter_upcoming_bookings(self, queryset, name, value):
        if value:
            return queryset.filter(start_date__gt=timezone.now())
        return queryset
