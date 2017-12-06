from django.test import TestCase
from day06 import day_06_1, day_06_2


class Day06Tests(TestCase):

    def setUp(self):
        self.example_data1 = [0, 2, 7, 0]

        self.data1 = []

        with open('day06/input') as raw_data:
            data = raw_data.read()

        for item in data.split('\t'):
            if item:
                self.data1.append(int(item))

    def test_day06(self):
        self.assertEqual(day_06_1(self.example_data1), 5)
        self.assertEqual(day_06_2(self.example_data1), 4)

        print("Day 06_1 answer", day_06_1(self.data1))
        print("Day 06_2 answer", day_06_2(self.data1))
