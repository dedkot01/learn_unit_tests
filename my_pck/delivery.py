from . import DetailsProvider


class Delivery:
    def __init__(self, details_provider: DetailsProvider):
        self.details_provider = details_provider

    def calculate_cost(self):              # рассчитывает стоимость доставки
        return self.details_provider.get_cost()

    def schedule_delivery(self):           # планирует доставку
        destination = self.details_provider.get_destination()
        cost = self.calculate_cost()
        return f"Доставка запланирована в город: {destination}. Стоимость: {cost} ₽."
