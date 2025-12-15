from django.urls import path
from django_exercise import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]