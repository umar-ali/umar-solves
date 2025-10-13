

def threeSumClosest(nums:list[int], target:int) -> int:
    nums.sort()
    ln = len(nums)
    mndf = []
    mxdf = []
    for i in range(ln-2):
        if i >= 1 and nums[i]== nums[i-1]:
            continue
        l = i+1
        r = ln-1
        while l < r:
            t = nums[i] + nums[l] + nums[r]
            if t == target:
                return t
            elif t < target:
                # print(t)
                mndf.append(target - t)
                l+=1
            else:
                mxdf.append(target - t)
                r-=1

    mn = min(mndf) if mndf else None
    mx = max(mxdf) if mxdf else None
    if mn is not None and mx is not None:
        if  mn < abs(mx):
            return target - mn
        else:
            return target + abs(mx)

    elif mn is not None:
        return target - mn
    elif mx is not None:
       return target + abs(mx)
    return target

if __name__ == "__main__":
    print(threeSumClosest([-1, 2, 1, -4], 1))
    print(threeSumClosest([0, -1, 1], 1))
    print(threeSumClosest([0, 0, 0], 1))
    print(threeSumClosest([0, 0, 3, 4], 4))
    print(threeSumClosest([-5, 2, 1, 9], 3))
    print(threeSumClosest([-5, 2, 1, 9], 8))
    print(threeSumClosest([-5, 2, 1, 9], -8))
    print(threeSumClosest([-4,2,2,3,3,3], 0))


