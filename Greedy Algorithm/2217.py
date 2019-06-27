rope_num = int(input())
rope_list = [int(input()) for _ in range(rope_num)]
rope_list.sort(reverse=True)

max_weight = 0

for i in range(rope_num):
    if i == 0:
        max_weight = rope_list[i]
        continue

    weight = rope_list[i] * (i + 1)

    if weight > max_weight:
        max_weight = weight

print(max_weight)
