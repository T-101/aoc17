from django.test import TestCase
from day01 import day01_1, day01_2


class Day01Tests(TestCase):

    def setUp(self):

        self.data1, self.data2 = [], []

        self.data1.append('1122')
        self.data1.append('1111')
        self.data1.append('1234')
        self.data1.append('91212129')

        with open('day01/input') as raw_data:
            data = raw_data.read()
            for item in data.split('\n'):
                if data:
                    self.data1.append(item)

        self.data2.append('1212')
        self.data2.append('1221')
        self.data2.append('123425')
        self.data2.append('123123')
        self.data2.append('12131415')

    def test_day_01(self):
        self.assertEqual(day01_1(self.data1[0]), 3)
        self.assertEqual(day01_1(self.data1[1]), 4)
        self.assertEqual(day01_1(self.data1[2]), 0)
        self.assertEqual(day01_1(self.data1[3]), 9)

        self.assertEqual(day01_2(self.data2[0]), 6)
        self.assertEqual(day01_2(self.data2[1]), 0)
        self.assertEqual(day01_2(self.data2[2]), 4)
        self.assertEqual(day01_2(self.data2[3]), 12)
        self.assertEqual(day01_2(self.data2[4]), 4)

        print("Day 01_1 answer", day01_1(self.data1[4]))
        print("Day 01_2 answer", day01_2(self.data1[4]))
