import random

# Naive String Matching
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)

    return matches, comparisons


# Compute LPS Array for KMP
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# KMP Search
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


# Rabin-Karp Search
def rabin_karp(text, pattern, q=101):
    d = 256

    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for s in range(n - m + 1):

        if p_hash == t_hash:
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)

        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


# ---------------- MAIN PROGRAM ----------------

attendance = "ARUN PRIYA KIRAN HARINI RAHUL KEERTHANA HARINI"

student = "HARINI"

print("Attendance List:")
print(attendance)

print("\nSearching for Student:", student)

m1, c1 = naive_search(attendance, student)
m2, c2 = kmp_search(attendance, student)
m3, c3 = rabin_karp(attendance, student)

print("\nNaive Search")
print("Found at positions:", m1)
print("Comparisons:", c1)

print("\nKMP Search")
print("Found at positions:", m2)
print("Comparisons:", c2)

print("\nRabin-Karp Search")
print("Found at positions:", m3)
print("Comparisons:", c3)


# Performance Comparison

large_text = " ".join(random.choices(
    ["ARUN", "PRIYA", "KIRAN", "HARINI", "RAHUL", "KEERTHANA"],
    k=3000
))

patterns = ["ARUN", "PRIYA", "HARINI", "KEERTHANA"]

print("\nPerformance Comparison")
print(f'{"Student":<12} {"Naive":<10} {"KMP":<10} {"RK":<10}')
print("-" * 45)

for p in patterns:
    _, c1 = naive_search(large_text, p)
    _, c2 = kmp_search(large_text, p)
    _, c3 = rabin_karp(large_text, p)

    print(f'{p:<12} {c1:<10} {c2:<10} {c3:<10}')