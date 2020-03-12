import unittest
import statistics

from Tree import *


class MyTestCase(unittest.TestCase):

    def test_tree(self):
        create_tree();
        nodes = [[5, 1], [3, 2], [7, 2], [2, 3], [5, 3], [0, 3], [1, 3], [8, 4], [2, 4], [5, 5]]
        visited_nodes(Node(5, 1))
        for node in nodes:
            self.assertEqual(node[0], search(node[0], node[1]).data)
            self.assertEqual(node[1], search(node[0], node[1]).lvl)

    @staticmethod
    def test_sum_data_in_tree():
        nodes1 = [[5, 1], [3, 2], [7, 2], [2, 3], [5, 3], [0, 3], [1, 3], [8, 4], [2, 4], [5, 5]]
        lists_of_trees = []
        # creating list of all possible trees
        for i in nodes1:
            tmp = []
            visited_nodes(search(i[0], i[1]))
            for el in list_of_visited_nodes:
                tmp.append(el.data)
            lists_of_trees.append(tmp)
            list_of_visited_nodes.clear()
        counter = 0
        # sum each possible tree
        for record in lists_of_trees:
            assert sum(record) == sum_data_in_tree(nodes1[counter][0], nodes1[counter][1])
            counter += 1

    @staticmethod
    def test_mean():
        nodes1 = [[5, 1], [3, 2], [7, 2], [2, 3], [5, 3], [0, 3], [1, 3], [8, 4], [2, 4], [5, 5]]
        lists_of_trees = []
        # creating list of all possible trees
        for i in nodes1:
            tmp = []
            visited_nodes(search(i[0], i[1]))
            for el in list_of_visited_nodes:
                tmp.append(el.data)
            lists_of_trees.append(tmp)
            list_of_visited_nodes.clear()
        counter = 0
        # calculate mean value for each possible tree
        for record in lists_of_trees:
            assert statistics.mean(record) == mean(nodes1[counter][0], nodes1[counter][1])
            counter += 1

    @staticmethod
    def test_median():
        nodes1 = [[5, 1], [3, 2], [7, 2], [2, 3], [5, 3], [0, 3], [1, 3], [8, 4], [2, 4], [5, 5]]
        lists_of_trees = []
        # creating list of all possible trees
        for i in nodes1:
            tmp = []
            visited_nodes(search(i[0], i[1]))
            for el in list_of_visited_nodes:
                tmp.append(el.data)
            lists_of_trees.append(tmp)
            list_of_visited_nodes.clear()
        counter = 0
        # calculate median value for each possible tree
        for record in lists_of_trees:
            assert statistics.median(record) == median(nodes1[counter][0], nodes1[counter][1])
            counter += 1


if __name__ == '__main__':
    unittest.main()
