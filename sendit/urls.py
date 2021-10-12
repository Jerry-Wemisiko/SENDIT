from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import parcel.views as parcel_views

router = routers.DefaultRouter()
router.register(r'users', parcel_views.UserViewSet)
router.register(r'orders', parcel_views.OrderViewSet)
router.register(r'locations', parcel_views.LocationViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', parcel_views.UserCreateAPIView.as_view(), name='register'),
    path('api/login/', parcel_views.UserLoginAPIView.as_view(), name='login'),
    path('api/logout/', parcel_views.logout_view, name='logout'),
]
