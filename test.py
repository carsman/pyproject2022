from unittest import TestCase
from convert import *

class Testing_t(TestCase):
    def test_temperature(self) -> None:
        cases =[
            (59, (15,"c", "f"))
            (161.33, (345, "k", "f"))
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, temperature(args))

class Testing_w(TestCase):
    def test_weight(self) -> None:
        cases =[
            (133.446653, (30,"n", "ft"))
            (1.700971, (60, "k", "f"))
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, weight(args))

class Testing_l(TestCase):
    def test_length(self) -> None:
        cases =[
            (3.94, (10,"cm", "inch"))
            (6400.8, (7, "yd", "ml"))
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, length(args))