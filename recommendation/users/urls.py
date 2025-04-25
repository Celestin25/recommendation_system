"""
URL mapping for users App APIs.
"""
from django.urls import path
from users import views


# ! FOR J.W.T Authentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'user'

urlpatterns = [
    path('', views.ListCreateUserView.as_view(), name='list-create'),
    path('<int:pk>/', views.DetailUserView.as_view(), name='user'),
    path('profile/', views.ManageProfileView.as_view(), name='profile'),
    path(
        'activate/<str:uidb64>/<str:token>/',
        views.ActivateAccountAPIView.as_view(),
        name='activate'
    ),

    # ! FOR J.W.T Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
