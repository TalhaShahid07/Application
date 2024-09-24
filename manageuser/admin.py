from django.contrib import admin
from .models import User, Location

# Custom admin class for the Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_name']  # Display ID and name of the location
    search_fields = ['id', 'location_name']  # Enable search by location name

# Custom admin class for the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_no', 'role', 'is_active']  # Essential fields displayed
    search_fields = ['first_name', 'last_name', 'email', 'phone_no', 'locations__location_name']  # Search by location name as well
    list_filter = ['role', 'is_active', 'locations']  # Add locations to the filter options

    # Fieldsets for organization in the admin interface
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone_no', 'role', 'is_active', 'locations')
        }),
    )
