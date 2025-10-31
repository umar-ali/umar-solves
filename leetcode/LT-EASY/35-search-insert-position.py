def search(l, r, nums, target):
    m = l + (r - l) // 2
    if nums[m] == target:
        return m
    elif l < r:
        if nums[m] < target:
            return search(m + 1, r, nums, target)
        else:
            return search(l, m, nums, target)
    else:
        if target < nums[m]:
            return l
        if target > nums[m]:
            return l + 1

def searchInsert(nums:list[int], target:int) -> int:
    ln = len(nums)
    if target <= nums[0]: 
        return 0
    elif target > nums[ln-1]:
        return ln
    
    #binary search
    def bin_search(start ,end) -> int:
        if start == end:
            return start

        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return bin_search(start, mid)
        else:
            return bin_search(mid+1, end)

    return bin_search(0, ln-1)
    
if __name__ == "__main__":
    nums = [1, 2, 5 ,6]
    target = 5
    assert searchInsert(nums, target) == search(0, len(nums) -1, nums, target)
    # print(searchInsert([1, 2, 5 ,6], 5)) #2
    # print(searchInsert([1, 3, 5 ,6], 2)) #1
    # print(searchInsert([1, 3, 5 ,6], 7)) #4
    # print(searchInsert([1], 1)) #0
    # print(searchInsert([1], 0)) #0
    # print(searchInsert([1], 2)) #1
    # print(searchInsert([1,3], 3)) #1
    # print(searchInsert([1,3, 5], 4)) #2
    # print(searchInsert([1,3, 5, 6], 6)) #3
    # print(searchInsert([1,3, 5, 10], 6)) #3
    # print(searchInsert([1,3, 5, 10], 5)) #2
    print(searchInsert([1,3, 5, 10], 6)) #3
    print(search(0, 3,[1,3, 5, 10], 6)) #3