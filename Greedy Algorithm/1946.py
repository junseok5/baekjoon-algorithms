def solution(N, data_list):
    data_list = sorted(data_list, key=lambda r: r[0])
    max_pass = 0
    min_intv = N

    for grade in data_list:
        if grade[1] < min_intv:
            min_intv = grade[1]
            max_pass = max_pass + 1

    return max_pass


result_list = []
TEST_CASE_NUM = int(input())

for _ in range(TEST_CASE_NUM):
    N = int(input())
    data_list = [list(map(int, input().split())) for _ in range(N)]
    result_list.append(solution(N, data_list))

for result in result_list:
    print(result)
