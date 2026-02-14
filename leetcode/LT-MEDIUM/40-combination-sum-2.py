from typing import List

def combinations(arr:list, target:int, start_idx:int, currComb:list, currSum:int, combs:List[List]):
    if currSum > target:
        #backtrack when sum exceeds our target
        return 
    elif currSum == target:
        #found the combo, add to cosmbs
        combs.append(currComb[:])
        return 
    else:
        #still less than target, try another combinations
        for i in range(start_idx, len(arr)):
            #skipping same number
            if i > start_idx and arr[i] == arr[i-1]:
                continue
            currComb.append(arr[i])
            currSum += arr[i]
            combinations(arr, target, i+1, currComb, currSum, combs)
            currComb.pop()
            currSum -= arr[i]

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    combs = [] #To keep track of combinations sum to target
    currComb = []
    combinations(candidates, target, 0, currComb, 0, combs)
    return combs

if __name__ == "__main__":
    ones = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(combinationSum2([3, 2, 5, 9, 1], 10))
    print(combinationSum2(ones, 30))
    print(combinationSum2([10,1,2,7,6,1,5], 8))
