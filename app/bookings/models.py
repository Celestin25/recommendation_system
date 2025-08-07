from django.db import models
from users.models import User
from inventory.models import Equipment
from bookings.choices import BOOKING_STATUS


class EquipmentBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=BOOKING_STATUS, default='pending')
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Add any addiional information here."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Check if this is a new booking
        if self.pk is None:
            self.equipment.quantity_available -= self.quantity

        previous = EquipmentBooking.objects.get(pk=self.pk)

        # check if the booking is just being changed to cancelled now
        if previous.status != 'cancelled' and self.status == 'cancelled':
            self.equipment.quantity_available += self.quantity
        # check if the booking is just being changed to completed now
        elif previous.status not in ['completed', 'cancelled'] and self.status == 'completed': # noqa
            self.equipment.quantity_available += self.quantity
        elif previous.status == 'cancelled' and self.status != 'cancelled':
            if self.status == 'completed':
                self.equipment.quantity_available += self.quantity
            else:
                self.equipment.quantity_available -= self.quantity

        if self.quantity > self.equipment.quantity_available:
            raise ValueError(
                f"We have just {self.equipment.quantity_available} {self.equipment.name} available for booking" # noqa
            )

        self.equipment.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.equipment.name} - {self.user.email} - {self.status}"
