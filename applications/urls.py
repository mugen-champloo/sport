from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('activate/<int:activation_code>/', ActivationApiView.as_view()),
    path('users/', QuerysetAPI.as_view())
]