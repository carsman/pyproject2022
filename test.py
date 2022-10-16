from unittest import TestCase
from project2022-1 import temperature
from project2022-1 import weight
from project2022-1 import length

class Testing(TestCase):
    def test_temperature(self) -> None:
        cases =[
            (59, (15,"c", "f"))
            (161.33, (345, "k", "f"))
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, temperature(args))

class Testing(TestCase):
    def test_weight(self) -> None:
        cases =[
            (133.446653, (30,"n", "ft"))
            (1.700971, (60, "k", "f"))
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, weight(args))

class Testing(TestCase):
    def test_length(self) -> None:
        cases =[
            (3.94, (10,"cm", "inch"))
            (6400.8, (7, "yd", "ml"))
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, length(args))