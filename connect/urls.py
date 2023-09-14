from django.urls import path, include
from .views import *

app_name = 'connect'
urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', UserDetailView.as_view(), name="user-info"),
]