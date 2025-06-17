

def solve(nums: list[int]) -> None:
    ln = len(nums)
    piv = -1
    #sub-problem: 1 find the pivot i.e., least from the right
    for i in range(ln-2, -1, -1):
        if nums[i] < nums[i+1]:
            piv = i
            break

    if piv == -1: # no least / in descending order
        nums.sort()
        return
    
    #sub-problem:2 -> swap the piv with next greatest in right of piv (from right)
    for i in range(ln-1, piv, -1):
        if nums[i] > nums[piv]:
            nums[i], nums[piv] = nums[piv], nums[i]
            break

    #sub-problem:3 -> reverse the right sub-array in ascending order
    l, r = piv+1, ln-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    
if __name__ =="__main__":
    testcases = (
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
    )
    
    solutions = (
        [1, 3, 2], #nextperm
        [1, 2, 3], # nextperm not possible, sorted
        [1, 5, 1], #nextperm
    )
    
    for tc, soln in zip(testcases, solutions):
        solve(tc) # in-place
        assert tc == soln, "Failed" 
        