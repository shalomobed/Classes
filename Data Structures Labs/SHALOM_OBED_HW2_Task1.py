
def get_all_pairs_shortest_path(graph):
    '''
    Based on Dijkstra’s algorithm, write a method named get_all_pairs_shortest_path(graph) 
    that takes an adjacency list of a weighted and undirected graph as input and returns a matrix (2D 
    list) representing the shortest paths between all pairs of nodes.
    '''
    vertices = sorted(graph.keys())
    n = len(vertices)

    vertex_to_idx = {v:i for i, v in enumerate(vertices)}

    dist_matrix = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist_matrix[i][i] = 0

    #Run Dijkstra from each vertex
    for src_label in vertices:
        src_idx = vertex_to_idx[src_label]

        #Run Dijkstra's algorithm from this source
        distances = dijkstra_adjacency_list(graph, src_label)

        #Fill in the matrix row for this source
        for dest_label, distance in distances.items():
            dest_idx = vertex_to_idx[dest_label]
            dist_matrix[src_idx][dest_idx] = distance

    return dist_matrix

def dijkstra_adjacency_list(graph, src):
    import heapq

    #Initialize distances
    distances = {v: float('inf') for v in graph}
    distances[src] = 0

    #Priority queue: (distance, vertex)
    pq = [(0, src)]
    visited = set()

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        #Explore neighbors
        for neighbor, weight in graph.get(u, []):
            if neighbor not in visited:
                new_dist = curr_dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

    return distances
    
weightedGraph = {
    '0': [('1', 2), ('2', 8), ('3', 3)],
    '1': [('0', 2), ('5', 7)],
    '2': [('0', 8), ('3', 4), ('4', 2)],
    '3': [('0', 3), ('2', 4), ('4', 1)],
    '4': [('2', 2), ('3', 1), ('5', 12)],
    '5': [('4', 12), ('1', 7)]
}

result = get_all_pairs_shortest_path(weightedGraph)

print("Shortest Path Matrix:")
for row in result:
    print([int(x) if x != float('inf') else 'inf' for x in row])