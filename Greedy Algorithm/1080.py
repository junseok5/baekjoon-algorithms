N, M = map(int, input().split())
A = [list(map(str, input())) for _ in range(N)]
B = [list(map(str, input())) for _ in range(N)]

convert_count = 0
for i in range(0, N - 2):
    for j in range(0, M - 2):
        if A[i][j] == B[i][j]:
            continue
        else:
            convert_count = convert_count + 1

            for x in range(i, i+3):
                for y in range(j, j+3):
                    if A[x][y] == "0":
                        A[x][y] = "1"
                    else:
                        A[x][y] = "0"

for i in range(0, N):
    for j in range(0, M):
        if A[i][j] != B[i][j]:
            convert_count = -1

print(convert_count)