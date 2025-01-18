from django.urls import path
from .views import FormRegistration

urlpatterns = [
    path('messages/', FormRegistration.as_view(), name='websitemesage'),
]
