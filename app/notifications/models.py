"""
Notifications DATABASE MODELS
"""
from django.db import models
from django.conf import settings
from notifications.choices import (
    NOTIFICATION_TYPES,
    NOTIFICATION_STATUS,
)


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=30, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=150)
    message = models.TextField()
    status = models.BooleanField(default=False, choices=NOTIFICATION_STATUS)
    sentAt = models.DateTimeField(auto_now_add=True)
