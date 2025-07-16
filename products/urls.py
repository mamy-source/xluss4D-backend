from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('auth/', RegisterView.as_view(), name='auth'),
]
