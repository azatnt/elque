from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', TokenObtainPairView.as_view(), name='signin'),
]
