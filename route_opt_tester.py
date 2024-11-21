import json
import networkx as nx
from src.ai_models.route_optimization import optimize_route

# Function to load a traffic graph from a JSON file
def load_traffic_graph(json_file):
    with open(json_file, 'r') as f:
        graph_data = json.load(f)
    
    traffic_graph = nx.Graph()
    
    # Add nodes to the graph
    for node in graph_data['nodes']:
        traffic_graph.add_node(node)
    
    # Add edges to the graph
    for edge in graph_data['edges']:
        # 'from' is the source node, 'to' is the target node, and 'traffic' is the edge weight
        traffic_graph.add_edge(edge['from'], edge['to'], weight=edge['traffic'])
    
    return traffic_graph

# Load traffic graph from the JSON file
traffic_graph = load_traffic_graph(r'C:\Users\admin\Desktop\Smart traffic management\Smart-Traffic-Management-System\datasets\traffic_graph.json')

# Define the optimize_route function to find the full path
def optimize_route(graph, start_node, end_node):
    # Use Dijkstra's algorithm to find the shortest path based on 'weight' (traffic level)
    shortest_path = nx.dijkstra_path(graph, source=start_node, target=end_node, weight='weight')
    return shortest_path

# Find the optimized route from Node_11 to Node_18 (adjust as needed)
route = optimize_route(traffic_graph, 'Node_1', 'Node_8')  # Adjust start and end nodes accordingly
print("Optimized Route:", route)
