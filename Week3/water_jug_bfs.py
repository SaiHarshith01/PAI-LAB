from collections import deque

def water_jug_bfs_3_states(a, b, c, target):
    start = (0, 0, 0)
    queue = deque()
    queue.append((start, []))
    visited = set()

    while queue:
        (x, y, z), path = queue.popleft()

        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))

        if x == target or y == target or z == target:
            return path + [(x, y, z)]

        next_states = [
            (a, y, z), (x, b, z), (x, y, c),
            (0, y, z), (x, 0, z), (x, y, 0),
            (x - min(x, b - y), y + min(x, b - y), z),
            (x - min(x, c - z), y, z + min(x, c - z)),
            (x + min(y, a - x), y - min(y, a - x), z),
            (x, y - min(y, c - z), z + min(y, c - z)),
            (x + min(z, a - x), y, z - min(z, a - x)),
            (x, y + min(z, b - y), z - min(z, b - y))
        ]

        for nx, ny, nz in next_states:
            if (nx, ny, nz) not in visited:
                queue.append(((nx, ny, nz), path + [(x, y, z)]))

    return None

# Run BFS
result = water_jug_bfs_3_states(8, 5, 3, 4)

print("BFS Solution (jug states only, minimal steps):\n")
if result:
    for step, state in enumerate(result, 1):
        print(f"Step {step}: {state}")
else:
    print("No solution exists for the given jug capacities and target.")