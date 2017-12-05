from django.test import TestCase
from day05 import day05_1, day05_2


class Day05Tests(TestCase):

    def setUp(self):
        self.example_data1 = [0, 3, 0, 1, -3]

        self.data1 = []
        with open('day05/input') as raw_data:
            data = raw_data.read()

        for row in data.split('\n'):
            if row:
                self.data1.append(int(row))

    def test_day05(self):
        self.assertEqual(day05_1(self.example_data1), 5)
        self.assertEqual(day05_2(self.example_data1), 10)

        print("Day 05_1 answer", day05_1(self.data1))
        print("Day 05_2 answer", day05_2(self.data1))
