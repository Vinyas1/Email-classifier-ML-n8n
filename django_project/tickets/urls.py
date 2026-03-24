from django.urls import path
from .views import classify_ticket

urlpatterns = [
    path("predict/", classify_ticket),
]