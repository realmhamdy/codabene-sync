from rest_framework import generics

from stock.api.serializers import CreateStockReadingSerializer
from stock.models import StockReading


class CreateStockReadingView(generics.CreateAPIView):

    serializer_class = CreateStockReadingSerializer

    def perform_create(self, serializer):
        StockReading.objects.filter(g_t_i_n=self.request.data["g_t_i_n"]).delete()
        return super().perform_create(serializer)

    def get_queryset(self):
        return StockReading.objects.all()
