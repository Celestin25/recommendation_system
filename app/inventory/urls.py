from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import (
    EquipmentViewSet,
    CategoriesListView,
)

router = DefaultRouter()
router.register('equipments', EquipmentViewSet)

app_name = 'inventory'

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoriesListView.as_view())
]
