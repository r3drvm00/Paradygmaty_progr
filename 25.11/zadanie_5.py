import math
import unittest

def cut_cakes(area: float, small_cakes: list[float]) -> bool:
    total_area_needed = sum([math.pi * r ** 2 for r in small_cakes])
    return total_area_needed <= area

class TestEngine5(unittest.TestCase):

    def test_1(self):
        self.assertEqual(cut_cakes(3.14, [0.99]), True)

    def test_2(self):
        self.assertEqual(cut_cakes(315, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), True)

    def test_3(self):
        self.assertEqual(cut_cakes(315, [1, 2, 3, 4, 5, 6]), True)

    def test_4(self):
        self.assertEqual(cut_cakes(315, [1, 2, 3, 4, 5, 6, 7]), False)

    def test_5(self):
        self.assertEqual(cut_cakes(10 ** 6, [10 ** 1, 10 ** 2, 10 ** 3]), False)

if __name__ == '__main__':
    unittest.main()