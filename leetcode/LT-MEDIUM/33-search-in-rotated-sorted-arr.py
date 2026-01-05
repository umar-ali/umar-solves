
def binary_search(nums:list[int],target:int, beg:int, end: int):
    print(beg, end)
    if beg > end:
        return -1

    mid = beg + (end - beg) // 2

    print(nums[mid])

    if nums[mid] == target:
        return mid
    
    #left is sorted
    if nums[mid] >= nums[beg]:
        if target >= nums[beg] and target < nums[mid]:
            return binary_search(nums, target, beg, mid-1)
        else:
            return binary_search(nums, target, mid+1, end)
    #right is sorted
    if target > nums[mid] and target <= nums[end]:
        return binary_search(nums, target, mid+ 1, end )
    else:
        return binary_search(nums, target, beg, mid-1)


    
    

def search(nums:list[int], target:int)->int:
    # O(logn) -> binary search?
    print("-"*50)
    print(nums,"target", target)
    return binary_search(nums, target,  0, len(nums) -1)
    print("-"*50)


if __name__ == "__main__":
    print(search([19, 24, 31, 43, 13], 13))
    print(search([24, 31, 43, 13, 19], 13))
    print(search([24, 31, 43, 13, 19], 31))
    print(search([13, 19, 24, 31, 43], 31))
    print(search([24, 31, 43, 13, 19], 32))
    print(search([5, 1, 3], 5))
