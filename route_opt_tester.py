import networkx as nx
from src.ai_models.route_optimization import optimize_route

# Create a traffic graph with nodes (locations) and weighted edges (traffic level)
traffic_graph = nx.Graph()
traffic_graph.add_edge('A', 'B', weight=5)
traffic_graph.add_edge('A', 'C', weight=2)
traffic_graph.add_edge('B', 'C', weight=1)
traffic_graph.add_edge('C', 'D', weight=3)

# Find the optimized route from A to D
route = optimize_route(traffic_graph, 'B', 'D')
print("Optimized Route:", route)
