

def majorityElement(nums:list[int]) -> int:
    counter = {}
    for i in nums:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1
        if counter[i] > len(nums)//2:
            return i

if __name__ == "__main__":
    print(majorityElement([1,3, 3]))
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
