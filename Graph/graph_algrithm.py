# -*- coding=utf-8 -*-
import sys
from enum import Enum
sys.path.append('..')
from data_structure import *

"""
WHITE: not visited
GREY:  visiting
BLACK: finished visiting
"""
Color = Enum('Color', ('WHITE', 'GREY', 'BLACK'))

"""
Represent Graph by adjecent list
"""
class Graph(object):
    def __init__(self):
        self.__vertexes = []
        self.__edges = []

    def adjs(self, v):
        return v.adjs

    def add_edge(self, s, f, weight):
        if self.edge(s, f) != None:
            return
        edge = Edge(s, f, weight)
        self.__edges.append(edge)
        self.add_vertex(s)
        self.add_vertex(f)
        s.add_adj(f)
        f.add_adj(s)

    def add_vertex(self, v):
        if v in self.__vertexes:
            return
        self.__vertexes.append(v)

    @property
    def edges(self):
        return self.__edges

    @property
    def vertexes(self):
        return self.__vertexes

    def edge(self, s, f):
        for edge in self.__edges:
            # 无向图
            if (edge.s == s and edge.f == f) or (edge.s == f and edge.f == s):
                return edge
        return None

    def __init_vertexes(self):
        for v in self.__vertexes:
            v.color = Color.WHITE
            v.parent = None
            v.weight = sys.maxsize

    # BFS search
    def BFS_visit(self, s):
        self.__init_vertexes()
        if s not in self.__vertexes:
            return
        s.color = Color.GREY
        to_be_searched = [s]
        while len(to_be_searched) != 0:
            v = to_be_searched.pop(0)
            v.color = Color.GREY
            for u in self.adjs(v):
                if u.color == Color.WHITE:
                    u.parent = v
                    to_be_searched.append(u)
            v.color = Color.BLACK

    # DFS search
    def DFS(self):
        self.__init_vertexes()
        for v in self.__vertexes:
            if v.color == Color.WHITE:
                self.DFS_visit(v)

    def DFS_visit(self, v):
        v.color = Color.GREY
        for u in self.adjs(v):
            if u.color == Color.WHITE:
                u.parent = v
                self.DFS_visit(u)
        v.color = Color.BLACK

    # Find a path starts from s and finishes at f
    def find_path(self, s, f):
        if s not in self.__vertexes or f not in self.__vertexes:
            return []
        if s == f:
            return [s]
        if f.parent == None:
            return []
        else:
            return self.find_path(s, f.parent)+[f]

    @staticmethod
    def compare(u, v):
        return u.weight-v.weight

    """
    Minimum spaning Tree
    Input:
        s: start vertex
    Output:
        None, the algrithm sets value for the parent of vertexes in the graph
    """
    def MST_Prim(self, s):
        self.__init_vertexes()
        s.weight = 0
        to_be_visited = MinPriorityQueue(self.vertexes, Graph.compare)
        u=to_be_visited.extract_min()
        while u != None:
            for v in self.adjs(u):
                if to_be_visited.has(v) == False:
                    continue
                e = self.edge(u, v)
                # 每个节点的weight保存的是当前发现的联通到现有MST的最短边的权重
                if e.weight < v.weight:
                    to_be_visited.decrease_key(v, e.weight)
                    v.parent = u
            u = to_be_visited.extract_min()


class Edge(object):
    def __init__(self, s, f, w):
        self.s = s
        self.f = f
        self.weight = w


class Vertex(object):
    def __init__(self, key=-1):
        self.key = key
        self.weight = sys.maxsize
        self.parent = None
        self.color = Color.WHITE
        self.__adjs = []

    def add_adj(self, adj):
        if adj in self.__adjs:
            return
        self.__adjs.append(adj)

    @property
    def adjs(self):
        return self.__adjs



