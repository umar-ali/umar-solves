

def maximumScore(nums:list[int]) -> int:
    ln = len(nums)
    pref_sum_table = [None for i in range(ln)]
    suff_min_table = [None for i in range(ln)]
    for i in range(ln):
        if i == 0:
            pref_sum_table[i] = nums[i]
        else:
            pref_sum_table[i] = pref_sum_table[i-1] + nums[i]
        
    for i in range(ln-1, -1, -1):
        if i == ln-1:
            suff_min_table[i] = nums[i]
        else:
            suff_min_table[i] = min(suff_min_table[i+1], nums[i])
    
    mx = None
    for i in range(ln-1):
        score = pref_sum_table[i] - suff_min_table[i+1]
        if mx is None or score > mx:
            mx = score
    return mx



if __name__ == "__main__":
    print(maximumScore( [10,-1,3,-4,-5]))
    print(maximumScore([-7, -5, 3]))
    print(maximumScore([1,1]))
    print(maximumScore([1,1,-2]))



