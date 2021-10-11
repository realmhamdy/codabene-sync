from django.db import transaction
from rest_framework import generics, response, views

from stock.api.serializers import CreateStockReadingSerializer
from stock.models import StockReading


class CreateStockReadingView(generics.CreateAPIView):

    serializer_class = CreateStockReadingSerializer

    def perform_create(self, serializer):
        StockReading.objects.filter(g_t_i_n=self.request.data["g_t_i_n"]).delete()
        return super().perform_create(serializer)

    def get_queryset(self):
        return StockReading.objects.all()


class SynchronizeStockReadingView(views.APIView):

    """
    Synchronization mechanism using select_for_update() and transaction.atomic()
    so stock readings for the same Global Trade Identification Number are locked
    from deleting, updating until the transaction is finished.
    """

    http_method_names = ("get",)

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        stock_reading = (
            StockReading.objects.select_for_update()
            .filter(g_t_i_n=request.query_params["g_t_i_n"])
            .first()
        )
        return response.Response(
            data={"expiry_date": stock_reading.expiry_date if stock_reading else None}
        )
