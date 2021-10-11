from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class StockReading(models.Model):
    g_t_i_n = models.CharField(
        max_length=64, verbose_name="Global trade identification number"
    )
    expiry_date = models.DateField()
    shop = models.ForeignKey(
        Shop, related_name="stock_readings", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.g_t_i_n
