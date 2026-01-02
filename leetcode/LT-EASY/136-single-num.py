

def singleNumber(nums:list[int]) -> int:
    s = set()
    sm = 0
    for n in nums:
        if n not in s:
            s.add(n)
            sm += n
        else:
            sm -= n
    return sm


if __name__ == "__main__":
    print(singleNumber([4,1,2,1,2]))
    print(singleNumber([-4,1,-2,1,-2]))
            