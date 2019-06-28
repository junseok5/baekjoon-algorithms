A, B = map(str, input().split())


def get_min_dif(str1, str2):
    temp_min = 0
    for i in range(len(str1)):
        if str1[i] is not str2[i]:
            temp_min = temp_min + 1

    return temp_min


dif_len = abs(len(A) - len(B))
min_dif = get_min_dif(A, B)

for i in range(1, dif_len + 1):
    A = " " + A
    temp_min_dif = get_min_dif(A, B) - i

    if temp_min_dif < min_dif:
        min_dif = temp_min_dif

print(min_dif)



