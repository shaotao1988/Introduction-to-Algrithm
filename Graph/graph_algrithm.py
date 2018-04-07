# -*- coding=utf-8 -*-

def BFS_visit(G, s):
    for v in G.vertex:
        v.color = WHITE
        v.parent = None
    s.color = GREY
    to_be_searched = [s]
    while len(to_be_searched) != 0:
        v = to_be_searched.pop(0)
        v.color = GREY
        for u in v.adjs():
            if u.color == WHITE:
                u.parent = v
                to_be_searched.append(u)
        v.color = BLACK


def DFS(G):
    for v in G.vertex:
        v.color = WHITE
        v.parent = None
    for v in G.vertex:
        if v.color == WHITE:
            DFS_visit(G, v)


def DFS_visit(G, v):
    v.color = GREY
    for u in v.adjs():
        if u.color == WHITE:
            u.parent = v
            DFS_visit(G, u)
    v.color = BLACK

