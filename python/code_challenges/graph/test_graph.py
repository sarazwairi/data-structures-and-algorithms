import pytest
from graph import Graph, Node



# Node can be successfully added to the graph
def test_add_node():
    graph=Graph()
    expected='sara'
    actual=graph.add_node('sara').value
    assert actual==expected

# An edge can be successfully added to the graph
# A graph with only one node and edge can be properly returned

def test_add_edge():
    graph=Graph()
    node=Node('start')
    node1=graph.add_node('sara')
    with pytest.raises(KeyError):
        graph.add_edge(node,node1)

# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes():
    graph=Graph()
    node1=graph.add_node('sara')
    node2=graph.add_node('zwairi')
    expected=2
    actual=len(graph.get_nodes())

    assert actual==expected

# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included

def test_get_neighbors():
    graph=Graph()
    node1=graph.add_node('sara')
    node2=graph.add_node('zwairi')
    graph.add_edge(node2,node1,2)
    neighbors=graph.get_neighbors(node2)
    assert len(neighbors)==1
    edge=neighbors[0]
    assert edge.vertex.value=='sara'

    assert edge.weight==2

# The proper size is returned, representing the number of nodes in the graph
def test_size():
    graph=Graph()
    graph.add_node('sara')
    expected=1
    actual=graph.size()
    assert actual==expected

# An empty graph properly returns null
def test_empty_graph():
    graph=Graph()
    expected=0
    actual=graph.size()
    assert actual==expected

