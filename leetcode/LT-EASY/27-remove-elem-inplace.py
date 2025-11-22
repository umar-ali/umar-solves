


def solve(nums:list[int], val:int) -> int:
    nums.sort()
    i = 0
    f_idx, l_idx = None, None
    ln = len(nums)
    while i < ln :
        if nums[i] == val:
            if f_idx  is None:
                f_idx = i
        elif f_idx is not None:
            l_idx = i
            break
        i+=1
    if l_idx is None and f_idx is not None:
        l_idx = ln
    if l_idx is None or f_idx is None:
        return ln
    temp = nums[f_idx:l_idx]
    nums[f_idx:] = nums[l_idx:] + temp
    return ln - (l_idx - f_idx)
    
if __name__ == "__main__":
    ps1 = [3,2,2,3]
    print(solve(ps1, 3), ps1) # 2, [2,2 ...]
    ps2 = [0,1,2,2,3,0,4,2]
    print(solve(ps2, 2), ps2) #5, [0,1,4,0,3,_,_,_]
    ps3 = []
    print(solve(ps3, 2), ps3) #0, []
    ps4 = [0,1,2,2,3,0,4,2]
    print(solve(ps4, 5), ps4) #8, [0,1,2,2,3,0,4,2]
    ps5 = [0,1,5,5,3,0,4,5]
    print(solve(ps5, 5), ps5) #5, [0,1,3,0,4,....]