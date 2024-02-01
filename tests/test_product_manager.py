from unittest.mock import patch

from my_pck import ProductManager


class TestProductManager:
    @patch("my_pck.ProductManager.check_availability", return_value=True)
    def test_purchase_product(self, mock_check_availability):
        pm = ProductManager()
        assert pm.purchase_product(0) == "Покупка совершена"

    @patch("my_pck.ProductManager.check_availability", return_value=False)
    def test_purchase_product_not_available(self, mock_check_availability):
        pm = ProductManager()
        assert pm.purchase_product(1) == "Продукт недоступен"
