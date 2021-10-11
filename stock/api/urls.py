from django.urls import path

from stock.api import views

app_name = "api"

urlpatterns = [
    path(
        "stock-readings/",
        views.CreateStockReadingView.as_view(),
        name="create_stock_reading",
    ),
    path(
        "synchronize/", views.SynchronizeStockReadingView.as_view(), name="synchronize"
    ),
]
