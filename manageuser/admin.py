# from django.contrib import admin
# from .models import User, Location
# from django.utils import timezone

# # Custom admin class for the Location model
# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ['id', 'location_name']  # Display ID and name of the location
#     search_fields = ['location_name']  # Enable search by location name

# # Custom admin class for the User model
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     # Fields to display in the list view
#     list_display = ['id', 'first_name', 'last_name', 'email', 'phone_no', 'role', 'is_active', 'created_at', 'updated_at']
    
#     # Search functionality for user fields
#     search_fields = ['first_name', 'last_name', 'email', 'phone_no']  # Search by name, email, and phone number
    
#     # Filters for the list view (e.g., by role or active status)
#     list_filter = ['role', 'is_active', 'created_at']  # Filter by role, active status, and creation date
    
#     # Enable editing of related locations (Many-to-Many relationship)
#     filter_horizontal = ['locations']  # Horizontal filter for Many-to-Many fields (locations)
    
#     # Fields to be editable directly in the list view (optional)
#     list_editable = ['is_active']  # Make 'is_active' field editable from the list view
    
#     # Actions in the admin panel
#     actions = ['soft_delete_users', 'restore_users']  # Custom actions for soft delete and restoring users

#     # Custom action to soft delete selected users
#     def soft_delete_users(self, request, queryset):
#         queryset.update(is_active=False)  # Mark the selected users as inactive
#         for obj in queryset:
#             obj.deleted_at = timezone.now()  # Set the 'deleted_at' timestamp
#             obj.save()
#         self.message_user(request, "Selected users were soft deleted successfully.")
    
#     soft_delete_users.short_description = "Soft delete selected users"
    
#     # Custom action to restore soft-deleted users
#     def restore_users(self, request, queryset):
#         queryset.update(is_active=True, deleted_at=None)  # Restore users by setting them active and clearing 'deleted_at'
#         self.message_user(request, "Selected users were restored successfully.")
    
#     restore_users.short_description = "Restore selected users"

#     # Customize the admin form layout for better management
#     fieldsets = (
#         ('Personal Information', {
#             'fields': ('first_name', 'last_name', 'email', 'phone_no')
#         }),
#         ('Location Information', {
#             'fields': ('locations',)
#         }),
#         ('Role and Notifications', {
#             'fields': ('role', 'send_notification')
#         }),
#         ('Status', {
#             'fields': ('is_active',)
#         }),
#     )

#     # Make these fields read-only
#     readonly_fields = ['created_at', 'updated_at', 'deleted_at']


from django.contrib import admin
from .models import User, Location

# Custom admin class for the Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_name']  # Display ID and name of the location
    search_fields = ['location_name']  # Enable search by location name

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
