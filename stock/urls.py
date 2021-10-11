from django.urls import include, path

app_name = "stock"

urlpatterns = [path("api/", include("stock.api.urls", namespace="api"))]
