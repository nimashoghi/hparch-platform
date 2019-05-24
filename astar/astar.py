from math import inf
from queue import PriorityQueue

maze = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

adjacent_square_deltas = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


def show_maze(maze, start=None, goal=None, solution=None):
    for i, row in enumerate(maze):
        for j, element in enumerate(row):
            if element == 1:
                print("#", end=" ")
            elif start is not None and (i, j) == start:
                print("s", end=" ")
            elif goal is not None and (i, j) == goal:
                print("e", end=" ")
            elif solution is not None and (i, j) in solution:
                print("x", end=" ")
            else:
                print("o", end=" ")
        print()


def all_possible_neighbors(*, maze, current):
    def is_out_of_bounds(x, y):
        def is_in_bounds(i, array):
            return i >= 0 and i < len(array)

        return not is_in_bounds(x, maze) or not is_in_bounds(y, maze[0])

    def is_wall(x, y):
        return maze[x][y] == 1

    current_x, current_y = current

    adjacent_squares = (
        (current_x + dx, current_y + dy) for dx, dy in adjacent_square_deltas
    )

    for x, y in adjacent_squares:
        if not is_out_of_bounds(x, y) and not is_wall(x, y):
            yield (x, y)


def edge_cost(*, current, neighbor):
    return 1


def manhattan_distance_heuristic(*, neighbor, goal):
    neighbor_x, neighbor_y = neighbor
    goal_x, goal_y = goal
    return ((neighbor_x - goal_x) ** 2) + ((neighbor_y - goal_y) ** 2)


def valid_neighbors(*, maze, cost_so_far, current, goal):
    for neighbor in all_possible_neighbors(maze=maze, current=current):
        cost = cost_so_far[current] + edge_cost(current=current, neighbor=neighbor)
        if neighbor not in cost_so_far or cost < cost_so_far[neighbor]:
            yield neighbor, cost


def make_path(dict, goal):
    yield goal
    if goal in dict:
        yield from make_path(dict, dict[goal])


def astar(*, maze, start, goal, heuristic=manhattan_distance_heuristic):
    frontier = PriorityQueue()
    frontier.put(start, 0)

    current_path = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        neighbors = valid_neighbors(
            maze=maze, cost_so_far=cost_so_far, current=current, goal=goal
        )

        for neighbor, g in neighbors:
            cost_so_far[neighbor] = g

            # the heuristic value (e.g. manhattan distance)
            h = heuristic(neighbor=neighbor, goal=goal)
            f = g + h

            frontier.put(neighbor, f)

            current_path[neighbor] = current

    return list(make_path(current_path, goal))[::-1]


start = (0, 0)
end = (len(maze) - 1, len(maze[0]) - 1)

expected = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 4), (6, 5), (7, 6)]

path = astar(maze=maze, start=start, goal=end)
print(path)
print(expected)
print(path == expected)
show_maze(maze, start=start, goal=end, solution=path)
