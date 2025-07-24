"""
Admin site configuration
"""

from django.contrib import admin
from users import models
from django.utils.translation import gettext as translate_text
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """
    The user model for admin
    """
    ordering = ['id']
    list_display = [
        'id', 'email', 'first_name', 'last_name',
        'is_active', 'is_staff', 'intake',
    ]
    search_fields = ['email', 'first_name', 'last_name']
    readonly_fields = ['last_login', 'date_joined', 'date_modified']

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                )
            }
        ),
        (
            translate_text('Personal Info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'short_bio',
                    'about_me',
                    'intake',
                    'course',
                    'profession',
                )
            }
        ),
        (
            translate_text('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            translate_text('Important dates'),
            {
                'fields': (
                    'last_login',
                    'date_joined',
                    'date_modified',
                )
            }
        )
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'first_name',
                    'last_name',
                    'short_bio',
                    'about_me',
                    'intake',
                    'course',
                    'profession',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
    )


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Config for Course Admin View
    """
    list_display = ['id', 'name', 'code', 'duration']
    search_fields = ['name', 'code', 'duration']
    ordering = ['id']

    fieldsets = (
        (
            translate_text('Course Information'),
            {
                'fields': (
                    'name',
                    'code',
                    'duration',
                    'description',
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'name',
                    'code',
                    'duration',
                    'description',
                )
            }
        ),
    )


@admin.register(models.Intake)
class IntakeAdmin(admin.ModelAdmin):
    """
    Config for Intake Admin View
    """
    list_display = ['id', 'name', 'start_date', 'end_date']
    search_fields = ['name']
    ordering = ['id']

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'name',
                    'start_date',
                    'end_date'
                )
            }
        ),
    )
