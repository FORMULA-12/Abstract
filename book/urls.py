from django.urls import path
from .views import MainView


urlpatterns = [
    path('<int:pk>', MainView.as_view(), name='book'),
]