from django.urls import path

from my_app import views

app_name = "my_app"
urlpatterns = [
    path("cars", views.cars, name="car-list")
]
