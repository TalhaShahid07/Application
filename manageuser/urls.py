from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserListCreateView, UserDetailView, UserUpdateView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user-edit'),
    path('users/<int:pk>/delete/', UserViewSet.as_view({'delete': 'destroy'}), name='user-soft-delete'),
]

# Include router URLs for viewset
urlpatterns += router.urls