my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    # Node 'A' connects to 'B' with a weight of 5, 'C' with a weight of 3, and 'E' with a weight of 11
    'B': [('A', 5), ('C', 1), ('F', 2)],  # Node 'B' connects to 'A', 'C', and 'F', with their respective weights
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],  # Node 'C' connects to 'A', 'B', 'D', and 'E'
    'D': [('C', 1), ('E', 9), ('F', 3)],  # Node 'D' connects to 'C', 'E', and 'F'
    'E': [('A', 11), ('C', 5), ('D', 9)],  # Node 'E' connects to 'A', 'C', and 'D'
    'F': [('B', 2), ('D', 3)]  # Node 'F' connects to 'B' and 'D'
}


def shortest_path(graph, start, target=''):
    # Initialize unvisited list with all nodes from the graph
    unvisited = list(graph)

    # Create a dictionary to store the shortest distance to each node from the start node
    # The distance to the start node is 0, and all others are initially set to infinity
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Create a dictionary to store the paths from the start node to each other node
    # Initially, the path for each node is an empty list
    paths = {node: [] for node in graph}

    # Add the start node to its own path as the first node
    paths[start].append(start)

    # Main loop: continue until all nodes have been visited
    while unvisited:
        # Find the node with the smallest known distance (the current node)
        current = min(unvisited, key=distances.get)

        # Loop over each neighboring node of the current node
        for node, distance in graph[current]:
            # If a shorter path to the neighbor is found, update the distance
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]

                # Update the path for the neighbor
                # If the last node in the current path for the neighbor is already the neighbor, overwrite it
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    # Otherwise, extend the path of the current node
                    paths[node].extend(paths[current])

                # Add the neighbor to its path
                paths[node].append(node)

        # Remove the current node from the unvisited list, marking it as processed
        unvisited.remove(current)

    # Set up the list of nodes to print based on whether a specific target is provided
    targets_to_print = [target] if target else graph

    # Loop through each target node and print the distance and path from the start node
    for node in targets_to_print:
        # Skip the start node itself in the output
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    # Return the final distances and paths from the start node to all other nodes
    return distances, paths


# Run the shortest_path function on the graph, starting from node 'A'
shortest_path(my_graph, 'A')
