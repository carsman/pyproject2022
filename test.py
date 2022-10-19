from unittest import TestCase
from convert import *


class Testing(TestCase):
    def test_temperature(self) -> None:
        self.assertEqual(12, temperature(12, "c", "c"))
        self.assertEqual(-249.15, temperature(24, "k", "c"))
        self.assertEqual(262.0388888889, temperature(12, "f", "k"))
        self.assertEqual(537.2222222222, temperature(999, "f", "c"))
        self.assertEqual(0, temperature(12, "blabla", "c"))

    def test_weight(self) -> None:
        self.assertEqual(12000, weight(12, "kg", "gr"))
        self.assertEqual(3059.16, weight(30, "n", "gr"))
        self.assertEqual(630.0002886203, weight(45, "stone", "lbs"))
        self.assertEqual(111552.76, weight(100000, "cwt british", "cwt usa"))
        self.assertEqual(0, weight(999, "blabla", "gr"))

    def test_length(self) -> None:
        self.assertEqual(3.93701, length(10, "cm", "inch"))
        self.assertEqual(10, length(1000, "cm", "m"))
        self.assertEqual(3600.001944, length(100, "yd", "inch"))
        self.assertEqual(3.2775192, length(999, "dm", "ft"))
        self.assertEqual(0, length(10, "blablabla", "inch"))
