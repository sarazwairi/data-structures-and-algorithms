from graph.graph import Graph

def get_edges(route_graph, city_list):
    for index, city in enumerate(city_list):
        i = 0
        for vertex in route_graph._adjacency_list:
            if city == vertex.value:
                city_list[index] = {'city': city, 'vertex': vertex}
                break
            i += 1
            if i == route_graph.size():
                raise KeyError(f'{city} has no flights connecting to it.')
    price = 0
    j = 0
    while j < len(city_list) - 1:
        route_check = route_graph.get_neighbors(city_list[j]['vertex'])
        k = 0
        for destination in route_check:
            if destination.vertex.value== city_list[j+1]['city']:
                price += destination.weight
                break
            k += 1
            if k == len(route_check):
                return False, '$0'
        j += 1

    return True, f'${price}'
if __name__== "__main__":
    # graph=Graph()
    # Pandora=graph.add_node("Pandora")
    # Arendelle=graph.add_node("Arendelle")
    # Metroville=graph.add_node("Metroville")
    # Monstroplolis=graph.add_node("Monstroplolis")
    # Narnia=graph.add_node("Narnia")
    # Naboo=graph.add_node("Naboo")
    # graph.add_edge(Pandora,Arendelle,82)
    # graph.add_edge(Arendelle,Pandora,82)
    # graph.add_edge(Arendelle,Metroville,99)
    # graph.add_edge(Metroville,Monstroplolis,105)
    # graph.add_edge(Monstroplolis,Narnia,26)
    # graph.add_edge(Monstroplolis,Naboo,42)
    # result=graph.breadth_first(Pandora)

    # print (get_edges(graph,['Pandora','Arendelle','Metroville']))

    graph=Graph()
    Pandora=graph.add_node("Pandora")
    Arendelle=graph.add_node("Arendelle")
    Metroville=graph.add_node("Metroville")
    Monstroplolis=graph.add_node("Monstroplolis")
    Narnia=graph.add_node("Narnia")
    Naboo=graph.add_node("Naboo")
    graph.add_edge(Pandora,Arendelle,82)
    graph.add_edge(Arendelle,Pandora,82)
    graph.add_edge(Arendelle,Metroville,99)
    graph.add_edge(Metroville,Monstroplolis,105)
    graph.add_edge(Monstroplolis,Narnia,26)
    graph.add_edge(Monstroplolis,Naboo,42)
    actual=get_edges(graph,['Pandora','Arendelle','Metroville'])
    assert actual==(True, '$181')
