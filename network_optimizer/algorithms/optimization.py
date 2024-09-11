import networkx as nx
from ..models import Node, Link, Wavelength, Path

def create_network_graph():
    G = nx.Graph()
    nodes = Node.objects.all()
    links = Link.objects.all()

    for node in nodes:
        G.add_node(node.id, name=node.name)

    for link in links:
        G.add_edge(link.source.id, link.destination.id, weight=link.distance, capacity=link.capacity)

    return G

def dijkstra_shortest_path(graph, source, destination):
    return nx.dijkstra_path(graph, source, destination, weight='weight')

def allocate_wavelength(path, available_wavelengths):
    # Simple first-fit wavelength allocation
    return available_wavelengths[0] if available_wavelengths else None

def optimize_network():
    graph = create_network_graph()
    paths = Path.objects.all()
    available_wavelengths = list(Wavelength.objects.all())

    for path in paths:
        shortest_path = dijkstra_shortest_path(graph, path.source.id, path.destination.id)
        print(f"Shortest path for {path.source.id} to {path.destination.id}: {shortest_path}")
        
        path_links = []
        for i in range(len(shortest_path)-1):
            try:
                link = Link.objects.get(source__id=shortest_path[i], destination__id=shortest_path[i+1])
                path_links.append(link)
            except Link.DoesNotExist:
                print(f"Link from {shortest_path[i]} to {shortest_path[i+1]} does not exist.")
        
        path.links.set(path_links)
        path.wavelength = allocate_wavelength(path, available_wavelengths)
        path.latency = sum(link.distance for link in path_links) / 200000 * 1000  # Approximate latency in ms
        path.save()

    return "Network optimization completed."
