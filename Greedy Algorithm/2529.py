K = int(input())
INEQUS = list(map(str, input().split()))

visited = [False for _ in range(10)]
result_list = []


def dfs(v, cnt, result):
    if cnt == K:
        result_list.append(result)
    else:
        for i in range(10):
            if not visited[i]:
                if INEQUS[cnt] == "<":
                    if v >= i:
                        continue
                else:
                    if v <= i:
                        continue

                visited[i] = True
                dfs(i, cnt + 1, result + str(i))

    visited[v] = False


for i in range(10):
    visited[i] = True
    dfs(i, 0, str(i))

print(result_list[len(result_list) - 1])
print(result_list[0])
