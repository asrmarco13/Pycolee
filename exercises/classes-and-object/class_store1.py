class Store:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_item(self, name: str, price: int):
        my_dict = {'name': name, 'price': price}
        self.items.append(my_dict)

    def stock_price(self) -> int:
        total = 0
        for item in self.items:
            total += item['price']

        return total

    def stock_price_comprehension(self) -> int:
        return sum(item['price'] for item in self.items)


"""
Uncomment this line for tests
stores = Store('casa')
stores.add_item('divano', 400)
stores.add_item('tv', 1000)
total_store = stores.stock_price_comprehension()
print('Total items price: {}'.format(total_store))
"""
