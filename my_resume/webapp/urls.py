from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageTemplateView.as_view(), name = 'HomePageTemplateView'),
]
