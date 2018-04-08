# -*- coding: utf-8 -*-

import unittest

from graph_algrithm import *

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_vertex(self):
        G = Graph()
        self.assertEqual(len(G.vertexes), 0)
        for i in range(0, 10):
            v = Vertex(i)
            G.add_vertex(v)
        self.assertEqual(len(G.vertexes), 10)
        G.add_vertex(G.vertexes[0])
        self.assertEqual(len(G.vertexes), 10)

    def test_add_edge(self):
        G = Graph()
        self.assertEqual(len(G.edges), 0)
        v = []
        for i in range(0, 10):
            v.append(Vertex(i))
        for i in range(0, 9):
            G.add_edge(v[i], v[i+1], i)
            self.assertEqual(len(G.vertexes), 2+i)
            self.assertEqual(len(G.edges), 1+i)

    def test_BFS_visit(self):
        G = Graph()
        v = []
        for i in range(0, 10):
            v.append(Vertex(i))
        for i in range(0, 9):
            G.add_edge(v[i], v[i+1], i)
        G.BFS_visit(v[0])
        self.assertEqual(G.find_path(v[0], v[9]), v)

    def test_DFS_visit(self):
        G = Graph()
        v = []
        for i in range(0, 10):
            v.append(Vertex(i))
        for i in range(0, 9):
            G.add_edge(v[i], v[i+1], i)
        G.DFS()
        self.assertEqual(G.find_path(v[0], v[9]), v)


if __name__ == "__main__":
    unittest.main()