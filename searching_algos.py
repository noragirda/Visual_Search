import heapq
def depth_first_search(grid, start, goal):
    stack = [start]# Stack to hold nodes for DFS
    visited = set()# Set to track visited nodes
    parent_coming_from = {start: None}# Dictionary to store each node's parent for path reconstruction

    while stack:
        current_node = stack.pop()
        visited.add(current_node)

        if current_node == goal:
            return reconstruct_path(parent_coming_from, start, goal)
        
        for neighbor in get_neighbors(grid, current_node):
            if neighbor not in visited:
                stack.append(neighbor)
                parent_coming_from[neighbor] = current_node

    return None
def breadth_first_search(grid, start, goal):
    queue = [start]
    visited = set()
    parent_coming_from = {start: None}

    while queue:
        current_node = queue.pop(0)
        visited.add(current_node)

        if current_node == goal:
            return reconstruct_path(parent_coming_from, start, goal)
        
        for neighbor in get_neighbors(grid, current_node):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent_coming_from[neighbor] = current_node

    return None
def a_star_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    g_score = {start: 0}
    parent_coming_from = {start: None}
    
    while open_set:
        _, current_node = heapq.heappop(open_set)

        # If we've reached the goal, reconstruct the path
        if current_node == goal:
            return reconstruct_path(parent_coming_from, start, goal)
        
        for neighbor in get_neighbors(grid, current_node):
            tentative_g_score = g_score[current_node] + 1  # Each move has a cost of 1
            
            # Only consider this path if it's better than any known path to the neighbor
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                parent_coming_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # Return None if there's no path to the goal
def heuristic(node, goal):
    # Use Manhattan distance as the heuristic
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)
def dijkstra_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    g_score = {start: 0}
    parent_coming_from = {start: None}
    
    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        # If we've reached the goal, reconstruct the path
        if current_node == goal:
            return reconstruct_path(parent_coming_from, start, goal)
        
        for neighbor in get_neighbors(grid, current_node):
            tentative_g_score = g_score[current_node] + 1  # Each move has a cost of 1
            
            # Only consider this path if it's better than any known path to the neighbor
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                parent_coming_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score, neighbor))

    return None  # Return None if there's no path to the goal
def uniform_cost_search(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))  # (cost, node)
    
    g_score = {start: 0}
    parent_coming_from = {start: None}
    
    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        # If we reached the goal, reconstruct the path
        if current_node == goal:
            return reconstruct_path(parent_coming_from, start, goal)
        
        for neighbor in get_neighbors(grid, current_node):
            tentative_g_score = g_score[current_node] + 1  # Each move has a cost of 1
            
            # Only consider this path if it's better than any known path to the neighbor
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                parent_coming_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (tentative_g_score, neighbor))

    return None  # Return None if there's no path to the goal
def reconstruct_path(parent_coming_from, start, goal):
    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = parent_coming_from[current_node]
    path.append(start)
    path.reverse()
    return path

def get_neighbors(grid, node):
    x, y = node
    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != "obstacle":
            neighbors.append((new_x, new_y))
    return neighbors 