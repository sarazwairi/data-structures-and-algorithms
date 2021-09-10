# add_node
# add_edge
# get_nodes
# get_neighbors
# size
from typing import Deque


class Node:
    def __init__(self,value):
        self.value=value

class Edge:
    def __init__(self,vertex,weight):
        self.vertex=vertex
        self.weight=weight
class Queue():
    def __init__(self):
        self.deque1=Deque()
    def enqueue(self,value):
        self.deque1.appendleft(value)
    def dequeue(self):
        return self.deque1.pop()
    def __len__(self):
        return len(self.deque1)
class Graph:
    def __init__(self):
        self._adjacency_list={}

    def add_node(self,value):
        node=Node(value)
        self._adjacency_list[node]=[]
        return node
    def size(self):
        return len(self._adjacency_list)

    def add_edge(self,vertex1,vertex2,weight=1):
        if vertex1 not in self._adjacency_list:
            raise KeyError("not found")
        if vertex2 not in self._adjacency_list:
            raise KeyError("not found")
        self._adjacency_list[vertex1].append(Edge(vertex2,weight))


    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self,vertex):
        return self._adjacency_list.get(vertex,[])

    def breadth_first(self,vertex1,action=(lambda x:None)):
        nodes=list()
        breadth=Queue()
        visited=set()

        breadth.enqueue(vertex1)
        visited.add(vertex1)

        while breadth:
            front=breadth.dequeue()
            action(front)
            # nodes.add(front)
            children=self.get_neighbors(front)
            for n in children:
               child=n.vertex
               if child is not visited:
                   visited.add(child)
                   breadth.enqueue(child)
        return nodes


if __name__== "__main__":
    graph=Graph()
    node1=graph.add_node("1")
    node2=graph.add_node("2")
    node3=graph.add_node("3")

    graph.add_edge(node1,node2)
    graph.add_edge(node1,node3)


    graph.breadth_first(node1,lambda v: print(v.value))

