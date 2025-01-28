from django.urls import path
from .views import FormRegistration , form_view

urlpatterns = [
    path('messages/', FormRegistration.as_view(), name='websitemesage'),
    path('data/' , form_view , name="form")
]
