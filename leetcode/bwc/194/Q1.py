def peakValleyDifference(nums: list[int]) -> int:

    i = 1
    pk = 0
    vy = 0 
    while i < len(nums) - 1:
        #peak
        if nums[i - 1 ] < nums[i] and nums[i+1] < nums[i]:
            pk+=nums[i]
        #valley
        elif nums[i - 1 ] > nums[i] and nums[i+1] > nums[i]:
            vy+=nums[i]
        i+=1
    return pk - vy


if __name__ == "__main__":
    c_1 = [1,5,2,4,1,3,0]
    c_2 = [-5,-6,-1,-2,5,3,2]
    c_3 = [6,5,2,5,5,3,6]
    print(peakValleyDifference(c_1))
    print(peakValleyDifference(c_2))
    print(peakValleyDifference(c_3))



