import networkx as nx

def optimize_route(traffic_graph, start, end):
    shortest_path = nx.shortest_path(traffic_graph, source=start, target=end, weight='traffic')
    return shortest_path
