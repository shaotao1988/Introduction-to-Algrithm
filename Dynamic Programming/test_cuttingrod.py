# -*- coding: utf-8 -*-

import unittest

from cuttingrod import *

class TestCuttingrod(unittest.TestCase):
    
    def setUp(self):
        self.price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.optimal_r = [0, 1, 5, 8, 10, 13, 17, 18, 22, 25, 30]

    def tearDown(self):
        pass

    def test_cuttingrod_topdown(self):
        for i in range(0, len(self.price)):
            self.assertEqual(cutting_rod_bruteforce(self.price, i), self.optimal_r[i])

    def test_cuttingrod_topdown(self):
        for i in range(0, len(self.price)):
            self.assertEqual(cutting_rod_topdown(self.price, i), self.optimal_r[i])

    def test_cuttingrod_bottomup(self):
        for i in range(0, len(self.price)):
            self.assertEqual(cutting_rod_bottomup(self.price, i), self.optimal_r[i])

if __name__ == "__main__":
    unittest.main()