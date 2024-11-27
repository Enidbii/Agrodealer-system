from django.urls import path, include

urlpatterns = [
    path("store/", include("Agrostore.backend.endpoints"))
]