from django.test import TestCase
from day04 import day04_1, day04_2


class Day04Tests(TestCase):
    def setUp(self):
        self.example_data1, self.example_data2 = [], []
        self.example_data1.append('aa bb cc dd ee')
        self.example_data1.append('aa bb cc dd aa')
        self.example_data1.append('aa bb cc dd aaa')

        self.example_data2.append('abcde fghij')
        self.example_data2.append('abcde xyz ecdab')
        self.example_data2.append('a ab abc abd abf abj')
        self.example_data2.append('iiii oiii ooii oooi oooo')
        self.example_data2.append('oiii ioii iioi iiio')

        with open('day04/input') as raw_data:
            data = raw_data.read()

        self.data1 = []

        for row in data.split('\n'):
            if row:
                self.data1.append(row)

    def test_day04(self):
        results = day04_1(self.example_data1)
        self.assertEqual(len(results), 2)
        results = day04_2(self.example_data2)
        self.assertEqual(len(results), 3)

        print("Day 04_1 answer: %r" % len(day04_1(self.data1)))
        print("Day 04_2 answer: %r" % len(day04_2(self.data1)))
