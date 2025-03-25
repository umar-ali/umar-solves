def search(l, r, nums, target):
    m = l + (r - l) // 2
    print(l, r, m)
    if nums[m] == target:
        return m
    elif l < r:
        if nums[m] < target:
            print("right")
            return search(m + 1, r, nums, target)
        else:
            print("left")
            return search(l, m, nums, target)
    else:
        if target < nums[m]:
            return l
        if target > nums[m]:
            return l + 1


if __name__ == "__main__":
    nums = [1]
    target = 2
    l = 0
    r = len(nums) - 1
    m = l + (r - l) // 2
    print(search(l, r, nums, target))
    
