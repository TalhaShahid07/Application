# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/products/', include('products.urls')),  # Products URLs
#     path('api/users/', include('users.urls')),  # Users URLs
#     path('api/', include('shift.urls')),  # Include shift app URLs
#     path('api/', include('manageuser.urls')),  # Include the manageuser app URLs under /api/ path

# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/products/', include('products.urls')),  # Products API URLs
    path('api/users/', include('users.urls')),  # Users API URLs
    path('api/shifts/', include('shift.urls')),  # Shifts API URLs
    path('api/manageuser/', include('manageuser.urls')),  # Manageuser app API URLs
]
