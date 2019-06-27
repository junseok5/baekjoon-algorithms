meeting_num = int(input())
meeting_input = []

for i in range(meeting_num):
    start, end = map(int, input().split())
    meeting_input.append((start, end))


def solution(meeting):
    start_time = 0
    meeting_count = 0

    meeting = sorted(meeting, key=lambda time: time[0])
    meeting = sorted(meeting, key=lambda time: time[1])

    for time in meeting:
        if time[0] >= start_time:
            start_time = time[1]
            meeting_count = meeting_count + 1

    return meeting_count


result = solution(meeting_input)
print(result)
