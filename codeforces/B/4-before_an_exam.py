YES = "YES"
NO = "NO"


def solve(d: int, sum_time: int, time_ranges: list[tuple[int]]):
    min_arr = []
    left_arr = []
    for t in time_ranges:
        print(t)
        sum_time -= t[0]
        min_arr.append(t[0])
        left_arr.append(t[1] - t[0])
    if not sum_time:
        print(YES)
        print(" ".join(map(str, min_arr)))
    elif sum_time < 0:
        print(NO)
    else:
        for i in range(d):
            if sum_time > left_arr[i]:
                sum_time -= left_arr[i]
                min_arr[i] = left_arr[i]
            else:
                min_arr[i] += sum_time
                sum_time = 0
                print(YES)
                print(" ".join(map(str, min_arr)))


if __name__ == "__main__":
    d, sum_time = tuple(map(int, input().split()))
    time_ranges = [tuple(map(int, input().split())) for _ in range(d)]
    solve(d, sum_time, time_ranges)
