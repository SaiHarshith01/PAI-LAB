import heapq

def heuristic(x, y, target):
    return min(abs(target - x), abs(target - y))

def water_jug_a_star(a, b, target):
    start = (0, 0)
    pq = []
    heapq.heappush(pq, (0, 0, start, []))
    visited = set()

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            return path

        next_states = [
            (a, y),  # fill jug A
            (x, b),  # fill jug B
            (0, y),  # empty jug A
            (x, 0),  # empty jug B
            (x - min(x, b - y), y + min(x, b - y)),  # pour A → B
            (x + min(y, a - x), y - min(y, a - x))   # pour B → A
        ]

        for nx, ny in next_states:
            if (nx, ny) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(nx, ny, target)
                heapq.heappush(pq, (new_f, new_g, (nx, ny), path))

    return None
result = water_jug_a_star(4, 3, 2)
print(result)