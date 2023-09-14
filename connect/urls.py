from django.urls import path, include
from .views import *


urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', UserDetailView.as_view(), name="user-info"),
]