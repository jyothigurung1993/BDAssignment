from django.urls import path
from .views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

"""
Url for user login and registration
"""
urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]