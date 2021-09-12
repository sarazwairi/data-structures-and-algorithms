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

    def breadth_first(self,vertex1=None,action=(lambda x:None)):
        nodes=list()
        breadth=Queue()
        visited=set()
        if not vertex1:
            return []
        breadth.enqueue(vertex1)
        visited.add(vertex1)
        while breadth:
            front=breadth.dequeue()
            action(front)
            nodes.append(front)
            children=self.get_neighbors(front)
            for n in children:
               child=n.vertex
               if child in visited:
                   continue
               else:
                   visited.add(child)
                   breadth.enqueue(child)
        return nodes


if __name__== "__main__":
    graph=Graph()
    Pandora=graph.add_node("Pandora")
    Arendelle=graph.add_node("Arendelle")
    Metroville=graph.add_node("Metroville")
    Monstroplolis=graph.add_node("Monstroplolis")
    Narnia=graph.add_node("Narnia")
    Naboo=graph.add_node("Naboo")
    graph.add_edge(Pandora,Arendelle)
    graph.add_edge(Arendelle,Pandora)
    graph.add_edge(Arendelle,Metroville)
    graph.add_edge(Metroville,Monstroplolis)
    graph.add_edge(Monstroplolis,Narnia)
    graph.add_edge(Monstroplolis,Naboo)
    result=graph.breadth_first(Pandora)
    result=[]
    result=graph.breadth_first(Pandora)
    actual=[node.value for node in result]
    print (actual)
