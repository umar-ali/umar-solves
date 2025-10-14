def fourSum(nums:list[int], target:int) -> list[list[int]]:
    res = []
    ln = len(nums)
    nums.sort()
    if ln < 4:
        return 4
    for i in range(ln-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, ln-2): 
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j + 1
            r = ln - 1
            while l < r:
                print(i, j, l, r)
                t = nums[i] + nums[j] + nums[l] + nums[r]
                if t == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                    
                elif t < target:
                    l+=1
                else:
                    r-=1

    return res


if __name__ == "__main__":
    print(fourSum([2,2,2,2,2], 8 )) #[[2,2,2,2]]
    print(fourSum([1, 0, -1, 0, -2, 2], 0)) #[[2,2,2,2]]
    print(fourSum([-2,-1,-1,1,1,2,2], 0))
