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

    def test_MST(self):
        G = Graph()
        v = []
        for i in range(0, 9):
            v.append(Vertex(i))
        G.add_edge(v[0], v[1], 4)
        G.add_edge(v[1], v[2], 8)
        G.add_edge(v[2], v[3], 7)
        G.add_edge(v[3], v[4], 9)
        G.add_edge(v[4], v[5], 10)
        G.add_edge(v[5], v[6], 2)
        G.add_edge(v[6], v[7], 1)
        G.add_edge(v[7], v[8], 7)
        G.add_edge(v[3], v[5], 14)
        G.add_edge(v[2], v[5], 4)
        G.add_edge(v[2], v[8], 2)
        G.add_edge(v[6], v[8], 6)
        G.add_edge(v[1], v[7], 11)
        G.add_edge(v[0], v[7], 8)
        G.MST_Prim(v[0])
        self.assertEqual(G.find_path(v[0], v[7]), [v[0], v[7]])
        self.assertEqual(G.find_path(v[0], v[4]), [v[0], v[7], v[6], v[5], v[2], v[3], v[4]])
        self.assertEqual(G.find_path(v[0], v[8]), [v[0], v[7], v[6], v[5], v[2], v[8]])



if __name__ == "__main__":
    unittest.main()