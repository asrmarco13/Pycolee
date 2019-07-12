class Store:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_item(self, name: str, price: int):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self) -> int:
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + ' - franchise')

    @staticmethod
    def store_details(store) -> str:
        total_price = store.stock_price()
        string_details = '{}, total stock price: {}'.format(store.name,
                                                            int(total_price))
        return string_details


"""
store1 = Store('Test')
store2 = Store('Amazon')
store2.add_item('keyboard', 160)

Store.franchise(store1)
Store.franchise(store2)

Store.store_details(store1)
Store.store_details(store2)
"""
