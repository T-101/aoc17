from django.test import TestCase
from day02 import day_02_1, day_02_2


class Day02Tests(TestCase):

    def setUp(self):

        self.example_data1, self.example_data2, self.data1 = [], [], []

        self.example_data1.append([5, 1, 9, 5])
        self.example_data1.append([7, 5, 3])
        self.example_data1.append([2, 4, 6, 8])

        self.example_data2.append([5, 9, 2, 8])
        self.example_data2.append([9, 4, 7, 3])
        self.example_data2.append([3, 8, 6, 5])

        with open('day02/input') as raw_data:
            data = raw_data.read()

        for row in data.split('\n'):
            if row:
                self.data1.append(list(map(int, row.split('\t'))))

    def test_day_02(self):
        self.assertEqual(day_02_1(self.example_data1), 18)
        self.assertEqual(day_02_2(self.example_data2), 9)

        print("Day 02_1 answer", day_02_1(self.data1))
        print("Day 02_2 answer", day_02_2(self.data1))
