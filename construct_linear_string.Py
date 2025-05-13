def construct_linear_string(kmers):
    graph = create_de_bruijn_graph(kmers)

    # Find an Eulerian path in the graph
    path = find_eulerian_path(graph)

    # Reconstruct the linear string from the Eulerian path
    linear_string = reconstruct_from_path(path)

    return linear_string

def create_de_bruijn_graph(kmers):
    graph = {}
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    # Find an Eulerian path using Hierholzer's algorithm
    path = []
    stack = []
    current_node = list(graph.keys())[0]  # Start from any node

    while True:
        if graph.get(current_node):
            stack.append(current_node)
            next_node = graph[current_node].pop()
            current_node = next_node
        else:
            path.append(current_node)
            if stack:
                current_node = stack.pop()
            else:
                break

    path.reverse()
    return path

def reconstruct_from_path(path):
    # Reconstruct the linear string from the Eulerian path
    linear_string = path[0]

    for i in range(1, len(path)):
        linear_string += path[i][-1]

    return linear_string

# Given 4-mer composition
kmers = [
    "AAAT", "AATG", "ACCC", "ACGC", "ATAC",
    "ATCA", "ATGC", "CAAA", "CACC", "CATA",
    "CATC", "CCAG", "CCCA", "CGCT", "CTCA",
    "GCAT", "GCTC", "TACG", "TCAC", "TCAT", "TGCA"
]

linear_string = construct_linear_string(kmers)

print(linear_string)
