def Solve(nums):
    i = 0
    while len(nums) != 1:
        n = len(nums)
        newNums = [0] * (n//2)
        while(i < n//2):
            if  == 1:
                newNums[i] = min(nums[2 * i] , nums[2 * i + 1])
                return newNums
            newNums[i] = min(nums[2 * i] , nums[2 * i + 1])
            newNums[i + 1] = max(nums[2 * (i+1)] , nums[2 * (i+1) + 1])
            i += 2
            print(newNums)
        nums = newNums
    return nums
          
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        nums = list(map(int, input().split()))
        print(Solve(nums))