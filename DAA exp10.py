import random
import time

comparisons = 0

# ---------------- Merge Sort ----------------
def merge(arr, l, m, r):
    global comparisons

    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

# ---------------- Heap Sort ----------------
def heapify(arr, n, i):
    global comparisons

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# ---------------- Test Runner ----------------
def run_merge(arr):
    global comparisons
    a = arr[:]
    comparisons = 0

    start = time.perf_counter()
    merge_sort(a, 0, len(a) - 1)
    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


def run_heap(arr):
    global comparisons
    a = arr[:]
    comparisons = 0

    start = time.perf_counter()
    heap_sort(a)
    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed

# ---------------- Test Cases ----------------
N = 5000

test_cases = {
    "Random": [random.randint(1, 100000) for _ in range(N)],
    "Sorted": list(range(N)),
    "Reverse": list(range(N, 0, -1)),
    "Nearly Sorted": list(range(N))
}

# Slight shuffle
ns = test_cases["Nearly Sorted"]
for _ in range(N // 20):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    ns[i], ns[j] = ns[j], ns[i]

# ---------------- Output ----------------
print(f'{"Input Type":<16} {"Merge Comps":>14} {"Merge Time(ms)":>16} '
      f'{"Heap Comps":>14} {"Heap Time(ms)":>16}')
print("-" * 80)

for case, arr in test_cases.items():
    m_comp, m_time = run_merge(arr)
    h_comp, h_time = run_heap(arr)

    print(f'{case:<16} {m_comp:>14} {m_time:>16.2f} '
          f'{h_comp:>14} {h_time:>16.2f}')