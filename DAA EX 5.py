import random

comparison_count = 0


# Divide and Conquer Method
def min_max_dc(arr, low, high):

    global comparison_count

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]

        return arr[high], arr[low]

    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


# Naive Method
def min_max_naive(arr):

    minimum = arr[0]
    maximum = arr[0]

    comparisons = 0

    for mark in arr[1:]:

        comparisons += 1
        if mark < minimum:
            minimum = mark

        comparisons += 1
        if mark > maximum:
            maximum = mark

    return minimum, maximum, comparisons


# ---------------- Main Program ----------------

marks = [78, 91, 65, 88, 95, 72, 84, 99, 69, 80]

comparison_count = 0

minimum, maximum = min_max_dc(marks, 0, len(marks) - 1)

dc_comparisons = comparison_count

_, _, naive_comparisons = min_max_naive(marks)

print("Student Marks")
print(marks)

print("\nLowest Mark :", minimum)
print("Highest Mark:", maximum)

print("\nDivide and Conquer Comparisons:", dc_comparisons)
print("Naive Method Comparisons:", naive_comparisons)


# ---------------- Performance Analysis ----------------

print("\nPerformance Comparison")
print(f'{"Students":<12}{"D&C":<10}{"Naive":<10}{"Formula":<10}')
print("-" * 45)

for size in [10, 100, 1000, 10000]:

    marks = [random.randint(35, 100) for _ in range(size)]

    comparison_count = 0

    min_max_dc(marks, 0, len(marks) - 1)

    dc = comparison_count

    _, _, naive = min_max_naive(marks)

    formula = 3 * size // 2 - 2

    print(f'{size:<12}{dc:<10}{naive:<10}{formula:<10}')