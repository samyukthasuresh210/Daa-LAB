def longest_common_subsequence(str1, str2):
    """
    Longest Common Subsequence using DP
    Time: O(m * n), Space: O(m * n)
    """
    m = len(str1)
    n = len(str2)

    # dp[i][j] = length of LCS of str1[:i] and str2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def print_lcs(dp, str1, str2):
    i = len(str1)
    j = len(str2)
    lcs = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))


def print_dp_table(dp, str1, str2):
    print("\nDP Table:")

    print("      ", end="")
    for ch in str2:
        print(f"{ch:>4}", end="")
    print()

    for i in range(len(dp)):
        if i == 0:
            print(" ", end=" ")
        else:
            print(str1[i - 1], end=" ")

        for j in range(len(dp[0])):
            print(f"{dp[i][j]:>4}", end="")
        print()


# Example strings
str1 = "AGGTAB"
str2 = "GXTXAYB"

print("String 1:", str1)
print("String 2:", str2)

dp = longest_common_subsequence(str1, str2)

print("\nLength of LCS:", dp[len(str1)][len(str2)])
print("Longest Common Subsequence:", print_lcs(dp, str1, str2))

print_dp_table(dp, str1, str2)