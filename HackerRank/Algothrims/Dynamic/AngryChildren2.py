#!/bin/python3

import itertools, sys
from math import inf

def angryChildren(K, packets):
    X = sorted(packets)
    S = list(itertools.accumulate(X))
    min_unfairness = unfairness = sum(i * X[i] - S[i - 1] for i in range(1, K))

    for i in range(1, N - K + 1):
        unfairness += (K - 1) * (X[i + K - 1] + X[i - 1])
        unfairness -= 2 * (S[i + K - 2] - S[i - 1])
        min_unfairness = min(min_unfairness, unfairness)

    return min_unfairness

if __name__ == "__main__":
    N = int(input().strip())
    K = int(input().strip())
    packets = []
    packets_i = 0
    for packets_i in range(N):
       packets_t = int(input().strip())
       packets.append(packets_t)
    result = angryChildren(K, packets)
    print(result)
