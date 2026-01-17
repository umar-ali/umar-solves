
def bin_search(nums:list[int], target:int, lo:int, hi:int) -> list[int]:
    if lo > hi:
        return [-1, -1]

    mid = lo + (hi - lo)//2

    if nums[mid] == target:
        st = mid 
        while st > 0 and nums[st - 1] == target:
            st -= 1

        ed = mid
        while ed < len(nums) - 1 and nums[ed + 1] == target:
            ed += 1
        return [st, ed]

    elif nums[mid] < target:
        return bin_search(nums, target, mid+1, hi)
    elif nums[mid] > target:
        return bin_search(nums, target, lo, mid -1)

    return [-1, -1]

def searchRange(nums:list[int], target:int) -> list[int]:
    lo = 0
    hi = len(nums) -1
    if len(nums) == 0:
        return [-1, -1]
    return bin_search(nums, target, lo, hi)

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    print(searchRange(nums, 8))
    nums = [5, 7, 7,8, 8,9,  10]
    print(searchRange(nums, 9))
    nums = [5, 7, 7,8, 8,9, 10]
    print(searchRange(nums, 6))
    print("-" * 50)
    nums = [2, 5]
    print(searchRange(nums, 5))
    print("-" * 50)
    nums = [1, 3]
    print(searchRange(nums, 1))
    nums = []
    print(searchRange(nums, 2))
