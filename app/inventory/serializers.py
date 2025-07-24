from rest_framework.serializers import ModelSerializer
from inventory.models import (
    Category,
    Supplier,
    Equipment,
    EquipmentImage,
    Resource,
    ResourceLink,
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]
        read_only_fields = ['id']


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'id',
            'name',
            'about',
            'address',
            'email',
            'phone_number',
            'website',
        ]
        read_only_fields = ['id']


class ResourceLinkSerializer(ModelSerializer):
    class Meta:
        model = ResourceLink
        fields = [
            'id',
            'title',
            'url',
            'resource'
        ]
        read_only_fields = ['id']


class ResourceSerializer(ModelSerializer):
    links = ResourceLinkSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Resource
        fields = [
            'id',
            'title',
            'description',
            'type',
            'file',
            'equipment',
            'links'
        ]
        read_only_fields = ['id']


class EquipmentImageSerializer(ModelSerializer):
    class Meta:
        model = EquipmentImage
        fields = [
            'id',
            'image',
            'equipment'
        ]
        read_only_fields = ['id']


class EquipmentSerializer(ModelSerializer):
    images = EquipmentImageSerializer(
        many=True, read_only=True, required=False)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Equipment
        fields = [
            'id',
            'name',
            'description',
            'categories',
            'quantity',
            'main_image',
            'status',
            'specifications',
            'potential_suppliers',
            'images',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
