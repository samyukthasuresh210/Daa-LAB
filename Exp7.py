def is_valid(current_sum, target):
    # Continue only if current sum does not exceed target
    return current_sum <= target


def solve_subset_sum(numbers, target):
    """
    Subset Sum using Backtracking
    Time: O(2^n)
    Space: O(n)
    """
    solutions = []
    backtrack_count = [0]

    def backtrack(index, subset, current_sum):
        if current_sum == target:
            solutions.append(subset[:])
            return

        if index == len(numbers):
            return

        # Include current element
        if is_valid(current_sum + numbers[index], target):
            subset.append(numbers[index])
            backtrack(index + 1, subset, current_sum + numbers[index])
            subset.pop()      # Undo choice
            backtrack_count[0] += 1

        # Exclude current element
        backtrack(index + 1, subset, current_sum)

    backtrack(0, [], 0)
    return solutions, backtrack_count[0]


def display_solutions(solutions):
    print("\nSubsets that achieve the target:")
    for i, subset in enumerate(solutions, 1):
        print(f" Solution {i}: {subset}")


# -------- Example --------
numbers = [2, 3, 5, 6, 8, 10]
target = 10

solutions, backtracks = solve_subset_sum(numbers, target)

print(f"Numbers: {numbers}")
print(f"Target Sum: {target}")
print(f"Solutions Found: {len(solutions)}")
print(f"Backtracks: {backtracks}")

display_solutions(solutions)