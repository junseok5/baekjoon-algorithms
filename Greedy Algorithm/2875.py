N, M, K = map(int, input().split())
result = 0

if N >= 2 and M >= 1:
    for i in range(K):
        if N < (2 * M):
            M = M - 1
        else:
            N = N - 1

    if N < (2 * M):
        result = N // 2
    else:
        result = M

print(result)
