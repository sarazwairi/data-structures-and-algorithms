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

# lab 36:Code Challenge:graph-breadth-first
# Pandora, Arendelle, Metroville, Monstroplolis, Narnia, Naboo
def test_breadth_first():
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
    actual=[node.value for node in result]
    assert actual==['Pandora','Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

def test_one_value_graph():
    graph=Graph()
    node=Node("Pandora")
    result=graph.breadth_first(node)
    actual=[node.value for node in result]
    assert actual==["Pandora"]

def test_empty_graph_breath():
    graph=Graph()
    result=graph.breadth_first()
    actual=[node.value for node in result]
    assert actual==[]

def test_depth_first():
    graph=Graph()

    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    node_c = graph.add_node("C")
    node_g = graph.add_node("G")
    node_d = graph.add_node("D")
    node_e = graph.add_node("E")
    node_h = graph.add_node("H")
    node_f = graph.add_node("F")
    graph.add_edge(node_a, node_b)
    graph.add_edge(node_a, node_d)
    graph.add_edge(node_b, node_c)
    graph.add_edge(node_c, node_g)
    graph.add_edge(node_b, node_d)
    graph.add_edge(node_d, node_e)
    graph.add_edge(node_d, node_f)
    graph.add_edge(node_d, node_h)
    graph.add_edge(node_f, node_h)
    breadth = graph.depth_first(node_a)
    actual = [vertex.value for vertex in breadth]
    assert actual==['A', 'B', 'C', 'G', 'D', 'E', 'F', 'H']

def test_empty_depth_first():
    graph=Graph()

    node_a = graph.add_node("A")
    node_b = graph.add_node("B")
    node_c = graph.add_node("C")
    node_g = graph.add_node("G")
    node_d = graph.add_node("D")
    node_e = graph.add_node("E")
    node_h = graph.add_node("H")
    node_f = graph.add_node("F")
    graph.add_edge(node_a, node_b)
    graph.add_edge(node_a, node_d)
    graph.add_edge(node_b, node_c)
    graph.add_edge(node_c, node_g)
    graph.add_edge(node_b, node_d)
    graph.add_edge(node_d, node_e)
    graph.add_edge(node_d, node_f)
    graph.add_edge(node_d, node_h)
    graph.add_edge(node_f, node_h)
    breadth = graph.depth_first()
    actual = [vertex.value for vertex in breadth]
    assert actual==[]
