from itertools import permutations

INF = float('inf')


def assignment_brute_force(cost, n):
    """
    Brute Force Assignment Problem
    Time: O(n!)
    Space: O(n)
    """
    best_cost = INF
    best_assignment = None

    # Generate all possible assignments
    for perm in permutations(range(n)):
        total_cost = 0
        for worker in range(n):
            total_cost += cost[worker][perm[worker]]

        if total_cost < best_cost:
            best_cost = total_cost
            best_assignment = perm

    return best_assignment, best_cost


# ----- Cost Matrix -----
cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

n = len(cost)

workers = ['W1', 'W2', 'W3', 'W4']
jobs = ['J1', 'J2', 'J3', 'J4']

best_assignment, best_cost = assignment_brute_force(cost, n)

print("Assignment Problem - Cost Matrix:")
print(f'{"":>5}', ' '.join(f'{j:>5}' for j in jobs))

for i, row in enumerate(cost):
    print(f'{workers[i]:>5}', ' '.join(f'{c:>5}' for c in row))

print("\nOptimal Assignment:")
for worker in range(n):
    print(f"{workers[worker]} --> {jobs[best_assignment[worker]]}")

print(f"\nMinimum Total Cost: {best_cost}")