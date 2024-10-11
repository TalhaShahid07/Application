from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/products/', include('products.urls')),  # Products API URLs
    path('api/users/', include('users.urls')),  # Users API URLs
    path('api/shifts/', include('shift.urls')),  # Shifts API URLs
    path('api/manageusers/', include('manageusers.urls')),  # Manageuser app API URLs
    # path('api/manageusers/', include('manageusers.urls')),  # Manageuser app API URLs

]
