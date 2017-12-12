from django.test import TestCase
from day08 import day_08_1, day_08_2


class Day08Tests(TestCase):
    def setUp(self):
        self.example_data1 = ['b inc 5 if a > 1',
                              'a inc 1 if b < 5',
                              'c dec -10 if a >= 1',
                              'c inc -20 if c == 10']

        self.data1 = []

        with open('day08/input') as raw_data:
            data = raw_data.read()

        for row in data.split('\n'):
            if row:
                self.data1.append(row)

    def test_day08(self):
        self.assertEqual(day_08_1(self.example_data1), 1)
        self.assertEqual(day_08_2(self.example_data1), 10)
        print("Day 08_1 Answer:", day_08_1(self.data1))
        print("Day 08_2 Answer:", day_08_2(self.data1))
