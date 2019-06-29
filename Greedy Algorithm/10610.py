from functools import reduce

num_input = input()
num_list = []
result = -1
total = 0

for n in num_input:
    num = int(n)
    num_list.append(num)
    total = total + num

if 0 in num_list and total % 3 is 0:
    num_list.sort(reverse=True)
    num_list = [str(n) for n in num_list]
    result = int(reduce(lambda a, b: a + b, num_list))

print(result)
