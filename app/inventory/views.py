from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiTypes,
    OpenApiParameter,
)
from rest_framework import viewsets, mixins, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from inventory import serializers
from inventory.permissions import IsAdminOrReadOnly
from inventory.models import (
    Category,
    Supplier,
    Equipment,
    EquipmentImage,
    Resource,
    ResourceLink,
)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'categories',
                OpenApiTypes.STR,
                description='Comma separated list of categories to filter by',
            ),
        ]
    )
)
class EquipmentViewSet(viewsets.ModelViewSet):
    """
    View for manage recipe APIs

    Image BASE_URL: https://res.cloudinary.com/ds8je77fy
    """
    serializer_class = serializers.EquipmentSerializer
    queryset = Equipment.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def _params_to_list(self, qs):
        return qs.split(',')

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'list':
            return serializers.EquipmentSerializer
        if self.action == 'upload_image':
            return serializers.EquipmentImageSerializer
        return self.serializer_class

    def get_queryset(self):
        categories = self.request.query_params.get('categories')
        # projects = self.request.query_params.get('projects')
        queryset = self.queryset

        if categories:
            categories_slugs = self._params_to_list(categories)
            queryset = queryset.filter(categories__name__in=categories_slugs)
        # if projects:
        #     projects_slugs = self._params_to_list(projects)
        #     queryset = queryset.filter(projects__id__in=projects_slugs)

        return queryset.order_by('-name').distinct()

    def perform_create(self, serializer):
        serializer.save()


class CategoriesListView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
