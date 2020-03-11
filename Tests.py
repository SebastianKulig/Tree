import unittest

from Tree import *


class MyTestCase(unittest.TestCase):


    def test_sum_data_in_tree(self):
        assert sum_data_in_tree(5, 1) == 38
        assert sum_data_in_tree(33, 1) == 0

    def test_mean(self):
        assert mean(5, 1) == 3.8
        assert mean(44, 2) == 0.0

    def test_median(self):
        assert median(5, 1) == 4.0
        assert mean(44, 2) == 0.0





if __name__ == '__main__':
    unittest.main()
