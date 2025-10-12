#Sum of elems with frequency div by k

from collections import defaultdict

def sumDivisibleByK(nums:list[int], k:int) -> int:
    freq = defaultdict(int)
    for n in nums:
        freq[n]+=1
    sm = 0
    for i in freq:
        if freq[i] % k == 0:
            sm += i * freq[i]
    return sm


if __name__ == "__main__":
    print(sumDivisibleByK([1,2,2,3,3,3,3,4], 2)) #16
    print(sumDivisibleByK([1,2,3,4,5], 2)) #0
    print(sumDivisibleByK([4,4,4,1,2,3], 3)) #0
