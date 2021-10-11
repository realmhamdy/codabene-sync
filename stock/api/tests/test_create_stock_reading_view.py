from django.urls import reverse
from rest_framework.test import APITestCase

from stock.models import Shop, StockReading


class TestCreateStockReadingView(APITestCase):
    def test_create_stock_reading(self):
        shop = Shop.objects.create(name="CodaBene")
        stock_reading = StockReading.objects.create(
            shop=shop, g_t_i_n="12345", expiry_date="2011-01-03"
        )

        response = self.client.post(
            reverse("stock:api:create_stock_reading"),
            data={"g_t_i_n": "12345", "expiry_date": "2013-01-29", "shop": shop.id},
        )

        self.assertEqual(response.status_code, 201)
        self.assertRaises(StockReading.DoesNotExist, stock_reading.refresh_from_db)
        self.assertTrue(
            StockReading.objects.get(
                g_t_i_n="12345", expiry_date="2013-01-29", shop=shop
            )
        )
