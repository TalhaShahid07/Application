from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:id>/', ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),
]
