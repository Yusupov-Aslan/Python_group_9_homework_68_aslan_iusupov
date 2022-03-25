from django.urls import path

from api_v1.views import add, subtract, multiply, divide

urlpatterns = [
    path("add/", add),
    path("subtract/", subtract),
    path("multiply/", multiply),
    path("divide/", divide),
]