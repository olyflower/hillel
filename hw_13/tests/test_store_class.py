import unittest

from ..store_class import Store, Mayonnaise, Ketchup, Mustard
s = Store([Mayonnaise('Легкий', 32, 120, 53), Ketchup('Шашличний', 35, 80, 35)], [Mustard('Французська', 26, 60, 39)])


class StoreTestCase(unittest.TestCase):
    def test_add_to_in_stock(self):
        s.add_to_in_stock(Mayonnaise('Легкий', 32, 120, 53))
        self.assertIn(Mayonnaise('Легкий', 32, 120, 53), s.in_stock)

    def test_add_in_sold(self):
        s.add_in_sold(Ketchup('Шашличний', 35, 80, 35))
        self.assertIn(Ketchup('Шашличний', 35, 80, 35), s.sold)
        self.assertNotIn(Ketchup('Шашличний', 35, 80, 35), s.in_stock)

    def test_rest_of_the_goods(self):
        s.add_to_in_stock(Ketchup('Шашличний', 35, 80, 35))
        s.rest_of_the_goods()
        self.assertNotEqual(s.rest_of_the_goods(), {})

    def test_profit_per_product(self):
        s.add_in_sold(Mustard('Французська', 26, 60, 39))
        s.profit_per_product()
        self.assertNotEqual(s.profit_per_product(), {})

    def test_total_profit_negative(self):
        self.assertEqual(abs(s.total_profit()), s.total_profit())


if __name__ == '__main__':
    unittest.main()
