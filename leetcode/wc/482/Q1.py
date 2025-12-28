

def maximumScore(nums:list[int]) -> int:
    ln = len(nums)
    mx = None
    for i in range(ln):
        prefx = nums[:i+1]
        suffx = nums[i+1:]
        if not prefx or not suffx:
            continue
        prefix_sum = sum(prefx)
        suffix_min = min(suffx) if suffx else 0
        score = prefix_sum - suffix_min
        print(i, prefix_sum, suffix_min, score)
        if mx is None or score > mx:
            mx = score
    return mx



if __name__ == "__main__":
    print(maximumScore( [10,-1,3,-4,-5]))
    print(maximumScore([-7, -5, 3]))
    print(maximumScore([1,1]))



