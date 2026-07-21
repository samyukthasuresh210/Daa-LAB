import time
import random

# Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            break

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Performance Analysis
def performance_analysis():
    sizes = [1000, 5000, 10000, 50000]

    print(f"{'Students':<10}{'IS Time(ms)':<15}{'BS Time(ms)':<15}")

    for size in sizes:
        roll_numbers = list(range(10001, 10001 + size))
        target = random.choice(roll_numbers)

        start = time.perf_counter()
        for _ in range(100):
            interpolation_search(roll_numbers, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()
        for _ in range(100):
            binary_search(roll_numbers, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:<10}{is_time:<15.4f}{bs_time:<15.4f}")


# Main Program
roll_numbers = [1001, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040, 1045]

target = 1030

index, comparisons = interpolation_search(roll_numbers, target)

print("Student Roll Numbers:", roll_numbers)
print("Searching for Roll Number:", target)

if index != -1:
    print("Student found at position:", index)
else:
    print("Student not found.")

print("Comparisons:", comparisons)

print("\nPerformance Analysis")
performance_analysis()