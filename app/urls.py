from rest_framework.routers import DefaultRouter
from .views import SalePointList
from django.urls import path

# router = DefaultRouter()
# router.register('salepoint/list', SalePointList, basename='sale_point')
# router.register('users', UserViewSet, basename='users')
# urlpatterns = router.urls

urlpatterns = [
    path('salepoints', SalePointList.as_view({'get': 'list'}), name='sale_point'),
    path('visit', SalePointList.as_view({'post': 'create'}), name='sale_point'),
]
