from django.urls import reverse
from rest_framework.test import APITestCase

from stock.models import Shop, StockReading


class TestSynchronizeStockReadingView(APITestCase):
    def test_GET_response(self):
        shop = Shop.objects.create(name="CodaBene")
        StockReading.objects.create(
            shop=shop, g_t_i_n="12345", expiry_date="2021-10-04"
        )

        response = self.client.get(reverse("stock:api:synchronize") + "?g_t_i_n=12345")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"expiry_date": "2021-10-04"})
