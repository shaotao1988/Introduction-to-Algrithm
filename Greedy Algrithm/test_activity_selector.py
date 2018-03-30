# -*- coding: utf-8 -*-

import unittest

from activity_selector import *

class TestActivitySelector(unittest.TestCase):
    
    def setUp(self):
        self.s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
        self.f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
        self.largest = 4

    def tearDown(self):
        pass

    def test_dynamic_selector(self):
        self.assertEqual(dynamic_activity_selector(self.s, self.f, len(self.s)), self.largest)

    def test_recursive_activity_selector(self):
        self.assertEqual(recursive_activity_selector(self.s, self.f, len(self.s)), self.largest)

    def test_iterative_activity_selector(self):
        self.assertEqual(iterative_activity_selector(self.s, self.f, len(self.s)), self.largest)

if __name__ == "__main__":
    unittest.main()