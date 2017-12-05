from django.test import TestCase
from day03 import day03_1, day03_2


class Day03Tests(TestCase):

    def setUp(self):
        self.data1 = 347991

    def test_day03(self):
        self.assertEqual(day03_1(1), 0)
        self.assertEqual(day03_1(12), 3)
        self.assertEqual(day03_1(23), 2)
        self.assertEqual(day03_1(1024), 31)

        print("Day 03_1 answer", day03_1(self.data1))
        print("Day 03_2 answer", day03_2(self.data1))
