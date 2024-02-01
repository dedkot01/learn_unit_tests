class ProductManager:
    def check_availability(self, product_id):
        # ... логика для проверки наличия продукта
        return True

    def purchase_product(self, product_id):
        if self.check_availability(product_id):
            # ... логика покупки продукта
            return 'Покупка совершена'
        else:
            return 'Продукт недоступен'
