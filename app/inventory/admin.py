from django.contrib import admin
from inventory import models
from django.utils.translation import gettext_lazy as _


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Config for Category Admin View
    """
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['id']

    fieldsets = (
        (
            _('Category Information'),
            {
                'fields': (
                    'name',
                    'description',
                )
            }
        ),
    )


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Config for Supplier Admin View
    """
    list_display = ['id', 'name', 'email',
                    'phone_number', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'phone_number']
    ordering = ['id']

    fieldsets = (
        (
            _('Supplier Information'),
            {
                'fields': (
                    'name',
                    'about',
                    'address',
                    'email',
                    'phone_number',
                    'website',
                )
            }
        ),
    )


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """
    Config for Equipment Admin View
    """
    list_display = ['id', 'name',
                    'quantity', 'status', 'created_at', 'updated_at']
    search_fields = ['name', 'status']
    ordering = ['id']

    fieldsets = (
        (
            _('Equipment Information'),
            {
                'fields': (
                    'name',
                    'description',
                    'categories',
                    'quantity',
                    'main_image',
                    'status',
                    'specifications',
                    'potential_suppliers',
                )
            }
        ),
    )


@admin.register(models.EquipmentImage)
class EquipmentImageAdmin(admin.ModelAdmin):
    """
    Config for Equipment Image Admin View
    """
    list_display = ['id', 'equipment', 'created_at', 'updated_at']
    search_fields = ['equipment__name']
    ordering = ['id']

    fieldsets = (
        (
            _('Equipment Image Information'),
            {
                'fields': (
                    'image',
                    'equipment',
                )
            }
        ),
    )


@admin.register(models.Resource)
class ResourcesAdmin(admin.ModelAdmin):
    """
    Config for Resources Admin View
    """
    list_display = ['id', 'title', 'type',
                    'equipment', 'added_at', 'updated_at']
    search_fields = ['title', 'type', 'equipment__name']
    ordering = ['id']

    fieldsets = (
        (
            _('Resource Information'),
            {
                'fields': (
                    'title',
                    'description',
                    'type',
                    'file',
                    'equipment',
                )
            }
        ),
    )


@admin.register(models.ResourceLink)
class ResourceLinkAdmin(admin.ModelAdmin):
    """
    Config for Resource Link Admin View
    """
    list_display = ['id', 'title', 'url',
                    'equipment', 'added_at', 'updated_at']
    search_fields = ['title', 'equipment__name']
    ordering = ['id']

    fieldsets = (
        (
            _('Resource Link Information'),
            {
                'fields': (
                    'title',
                    'url',
                    'equipment',
                )
            }
        ),
    )
