from django.urls import path
from bookings import views


urlpatterns = [
    path('', views.BookingList.as_view(), name='booking-list'),
    path('<int:pk>/', views.BookingDetail.as_view(), name='booking-list'),
    path('me/', views.UserBookingList.as_view(), name='user-booking-list'),
    path('me/<int:pk>/', views.ManageUserBooking.as_view(), name='manage-user-booking'),
]
