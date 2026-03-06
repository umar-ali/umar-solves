def findDuplicates(nums: list[int]) -> list[int]:
    res = []
    ln = len(nums)
    for i in range(ln):
        n = nums[i]
        if n == i + 1:
            i+=1
        elif n == nums[n -1]:
            res.append(n)
        else:
            nums[i] = nums[n-1]
            nums[n-1] = n
    return res


if __name__ == "__main__":
    print(findDuplicates([5,4,6,7,9,3,10,9,5,6])) #[9, 5, 6]

