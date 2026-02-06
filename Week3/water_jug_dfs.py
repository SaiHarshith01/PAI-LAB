def water_jug_dfs_3_states(a, b, c, target):
    start = (0, 0, 0)
    stack = [(start, [])]
    visited = set()

    while stack:
        (x, y, z), path = stack.pop()

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

        # reverse for DFS order
        for nx, ny, nz in reversed(next_states):
            if (nx, ny, nz) not in visited:
                stack.append(((nx, ny, nz), path + [(x, y, z)]))

    return None

# Run DFS
result = water_jug_dfs_3_states(8, 5, 3, 4)

print("DFS Solution (jug states only):\n")
if result:
    for step, state in enumerate(result, 1):
        print(f"Step {step}: {state}")
else:
    print("No solution exists for the given jug capacities and target.")