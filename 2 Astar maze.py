def heuristic(x1, y1, x2, y2):
    # Estimated steps left (no diagonals): just "how far in blocks"
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze, start, goal):
    # Maze size
    rows = len(maze)
    cols = len(maze[0])

    # This is where we store the next positions to check
    open_list = [start]

    # Store the steps we’ve taken
    came_from = {}

    # This tells how far we’ve walked so far
    g_score = {}
    g_score[start] = 0

    while open_list:
        # Find position with smallest score = steps so far + estimate left
        current = min(open_list, key=lambda pos: g_score[pos] + heuristic(pos[0], pos[1], goal[0], goal[1]))

        if current == goal:
            # If we reached the goal, build the path back!
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        open_list.remove(current)

        # Check up, down, left, right
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = current[0] + dx
            y = current[1] + dy
            neighbor = (x, y)

            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0:
                new_g = g_score[current] + 1

                if neighbor not in g_score or new_g < g_score[neighbor]:
                    g_score[neighbor] = new_g
                    came_from[neighbor] = current
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return None  # If no path found


maze = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = a_star(maze, start, goal)
print("Path:", path)
