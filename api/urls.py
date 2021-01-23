from django.urls import path, include
from .api_view import CategoryListAPIView



urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
]