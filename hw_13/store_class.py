"""Program for a store that sells 3 types of goods - mayonnaise, ketchup and mustard.

The program:
show how much is left of each product
what is the seller's current profit for each product
what is the seller's total profit
"""


# Сoefficient of markup on the price of goods for calculating profit
COEFFICIENT = 0.25


class SaveToFileMixin:
    def save_to_file(self, filename):
        result = self.serialize()
        with open(filename, 'w') as f:
            f.write(result)
        print('Saving to file done')

    def load_from_file(self, filename):
        with open(filename) as f:
            result = f.read()
        self.deserialize(result)
        print('Reading from file is done')


class Store(SaveToFileMixin):
    def __init__(self, in_stock, sold):
        self.in_stock = in_stock
        self.sold = sold

    def add_to_in_stock(self, product):
        self.in_stock.append(product)

    def add_in_sold(self, product):
        if product in self.in_stock:
            self.sold.append(product)
            self.in_stock.remove(product)

    def rest_of_the_goods(self):
        """Return the rest of the products in the store, displays the name and quantity of the product.
        """
        result = {}
        for product in self.in_stock:
            name = type(product).__name__
            if name in result.keys():
                result[name] += 1
            else:
                result[name] = 1
        return result

    def profit_per_product(self):
        """Return the profit for each sold product.

        Profit for each sold product take equal multiplying the price
        of the product sold by the markup coefficient.
        """
        result = {}
        for product in self.sold:
            name = type(product).__name__
            if name in result.keys():
                result[name] += product.price * COEFFICIENT
            else:
                result[name] = product.price * COEFFICIENT
        return result

    def total_profit(self):
        """Return the total profit for all products sold.

        The total profit is considered by multiplying the price of the item sold by the markup coefficient.
        """
        profit = 0
        for product in self.sold:
            profit += product.price * COEFFICIENT
        return profit

    def serialize(self):
        result = []
        for product in self.in_stock:
            result.append(f'{product.name} - {product.price}')
        return '\n'.join(result)

    def deserialize(self, raw_str):
        list_of_sentences = raw_str.split('\n')
        result = []
        for sentence in list_of_sentences:
            result.append(tuple(sentence.split(' - ')))
        self.in_stock = result


class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class Mayonnaise(Product):
    """Class of the product mayonnaise.
    """
    def __init__(self, name, price, weight, fat_content):
        super().__init__(name, price, weight)
        self.fat_content = fat_content

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price \
               and self.weight == other.weight \
               and self.fat_content == other.fat_content


class Ketchup(Product):
    """Class of the product ketchup.
    """
    def __init__(self, name, price, weight, amount_of_dry_matter):
        super().__init__(name, price, weight)
        self.amount_of_dry_matter = amount_of_dry_matter

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price \
               and self.weight == other.weight \
               and self.amount_of_dry_matter == other.amount_of_dry_matter


class Mustard(Product):
    """Class of the product mustard.
    """
    def __init__(self, name, price, weight, bitterness):
        super().__init__(name, price, weight)
        self.bitterness = bitterness

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price \
               and self.weight == other.weight \
               and self.bitterness == other.bitterness


def store_test():
    store = Store([
        *[Mayonnaise('Легкий', 32, 120, 53) for _ in range(30)],
        *[Mayonnaise('Провансаль', 45, 115, 67) for _ in range(10)],
        *[Ketchup('Шашличний', 35, 80, 35) for _ in range(10)],
        *[Ketchup('Чілі', 30, 75, 34) for _ in range(5)],
        *[Mustard('Гостра', 25, 60, 40) for _ in range(40)],
        *[Mustard('Американська', 27, 60, 35) for _ in range(55)],
        *[Mustard('Французська', 26, 60, 39) for _ in range(20)]
    ], [
        *[Mustard('Гостра', 25, 60, 40) for _ in range(20)],
        Ketchup('Шашличний', 40, 80, 35),
        *[Mayonnaise('Провансаль', 45, 115, 67) for _ in range(10)]
    ])

    store.add_in_sold(Mayonnaise('Легкий', 32, 120, 53))
    store.rest_of_the_goods()
    print(store.rest_of_the_goods())
    print(store.profit_per_product())
    print(store.total_profit())
    store.save_to_file('in_stock.txt')
    another_store = Store(Mayonnaise('Легкий', 32, 120, 53), Ketchup('Шашличний', 40, 80, 35))
    another_store.load_from_file('in_stock.txt')
    print(another_store.in_stock)


if __name__ == '__main__':
    store_test()
