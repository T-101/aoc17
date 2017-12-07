from django.test import TestCase
from day07 import day07_1


class Day07Tests(TestCase):
    def setUp(self):
        self.example_data1 = ["pbga (66)",
                              "xhth (57)",
                              "ebii (61)",
                              "havc (66)",
                              "ktlj (57)",
                              "fwft (72) -> ktlj, cntj, xhth",
                              "qoyq (66)",
                              "padx (45) -> pbga, havc, qoyq",
                              "tknk (41) -> ugml, padx, fwft",
                              "jptl (61)",
                              "ugml (68) -> gyxo, ebii, jptl",
                              "gyxo (61)",
                              "cntj (57)"]

        self.data1 = []

        with open('day07/input') as raw_data:
            data = raw_data.read()

        for row in data.split('\n'):
            if row:
                self.data1.append(row)

    def test_day07(self):
        self.assertEqual(day07_1(self.example_data1), 'tknk')
        print("Day 07_1 answer", day07_1(self.data1))
