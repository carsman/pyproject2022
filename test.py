from unittest import TestCase
from convert import *


class Testing(TestCase):
    def test_temperature(self) -> None:
        a = '12'
        b = 12, "c", "c"
        self.assertEqual(12, temperature(12, "c", "c"))

    def test_weight(self) -> None:
        cases = [
            (133.446653, (30, "n", "ft")),
            (1.700971, (60, "k", "f")),
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, weight(args))

    def test_length(self) -> None:
        cases = [
            (3.94, (10, "cm", "inch")),
            (6400.8, (7, "yd", "ml")),
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, length(args))
