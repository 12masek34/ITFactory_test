from .views import SalePointList
from django.urls import path



urlpatterns = [
    path('salepoints', SalePointList.as_view({'get': 'list'}), name='sale_point'),
    path('visit', SalePointList.as_view({'post': 'create'}), name='sale_point'),
]
