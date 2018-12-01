from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutPageView.as_view(), name='about')
]