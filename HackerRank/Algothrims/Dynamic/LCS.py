#!/bin/python3

import sys

def longestCommonSubsequence(a, b, m, n):
    # dynamic programming matrix
    dpm = [x[:] for x in [[0] * (n + 1)] * (m + 1)]

    # loop through to find the longest length LCS and build a dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dpm[i][j] = dpm[i-1][j-1] + 1
            else:
                dpm[i][j] = max(dpm[i][j-1], dpm[i-1][j])
    i = m
    j = n
    subsequence = []

    # backtrack to build a subsequence
    while dpm[i][j] is not 0:
        if(a[i - 1] == b[j - 1]):
            subsequence += [a[i - 1]]
            j -= 1;
            i -= 1;
        elif(dpm[i][j - 1] > dpm[i - 1][j]):
            j -= 1;
        else:
            i -= 1;


    return subsequence[::-1]

if __name__ == "__main__":
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    result = longestCommonSubsequence(a, b, m, n)
    print (" ".join(map(str, result)))
