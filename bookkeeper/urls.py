from django.urls import path
from bookkeeper import views

urlpatterns = [
    path("", views.home, name="home"),
]
