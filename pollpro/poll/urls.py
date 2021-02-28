from poll.views import RegisterView,MyObtainTokenPairView,LogoutView
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='create'),
    path('login/', MyObtainTokenPairView.as_view(),name='login-create'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout')
]
