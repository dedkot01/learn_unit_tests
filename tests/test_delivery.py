from unittest.mock import Mock

from my_pck import Delivery


class TestDelivery:
    def test_schedule_delivery(self):
        mock_details_provider = Mock()
        mock_details_provider.get_cost.return_value = 500
        mock_details_provider.get_destination.return_value = "Москва"

        delivery = Delivery(mock_details_provider)

        assert delivery.schedule_delivery() == "Доставка запланирована в город: Москва. Стоимость: 500 ₽."
