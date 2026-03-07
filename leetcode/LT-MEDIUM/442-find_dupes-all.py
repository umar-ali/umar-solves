def findDuplicates(nums: list[int]) -> list[int]:
    res = []
    nums.sort()
    ln = len(nums)
    i = 1

    while i < ln:
        if nums[i] == nums[i -1]:
            res.append(nums[i])
            i+=2
        else:
            i+=1
    return res




if __name__ == "__main__":
    print(findDuplicates([4,3,2,7,8,2,3,1])) #[2, 3]
    print(findDuplicates([5,4,6,7,9,3,10,9,5,6])) #[9, 5, 6]

