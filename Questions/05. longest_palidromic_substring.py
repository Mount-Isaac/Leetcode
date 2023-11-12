def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = ""

    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
        res = s[i]

    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            res = s[i:i+2]

    # Check for substrings of length > 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if k > len(res):
                    res = s[i:j+1]

    return res