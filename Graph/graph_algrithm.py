# -*- coding=utf-8 -*-
from enum import Enum

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
            if edge.s == s and edge.f == f:
                return edge
        return None

    def __init_vertexes(self):
        for v in self.__vertexes:
            v.color = Color.WHITE
            v.parent = None

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


class Edge(object):
    def __init__(self, s, f, w):
        self.s = s
        self.f = f
        self.weight = w


class Vertex(object):
    def __init__(self, key=-1):
        self.key = key
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



