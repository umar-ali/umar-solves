

def insert(intervals:list[list[int]], newInterval:list[int]) -> list[list[int]]:
    res = []
    new_st = newInterval[0]
    new_ed = newInterval[1]

    n = len(intervals)
    i = 0 
    while i < n and new_st > intervals[i][1]:
        res.append(intervals[i])
        i+=1

    while i < n and intervals[i][0] <= new_ed:
        new_st = min(new_st, intervals[i][0])
        new_ed = max(new_ed, intervals[i][1])
        i+=1

    res.append([new_st, new_ed])

    res.extend(intervals[i:])
    return res

if __name__ == "__main__":
    print(insert([[1,3],[6,9]], [2,5])) #  [[1,5],[6,9]]
