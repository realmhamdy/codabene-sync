from rest_framework import serializers

from stock.models import StockReading


class CreateStockReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockReading
        fields = ("g_t_i_n", "expiry_date", "shop")
