def combinations(arr:list, target:int, start_idx:int, currComb:list, currSum:int, combs:list[list]):
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
            currComb.append(arr[i])
            currSum += arr[i]
            combinations(arr, target, i, currComb, currSum, combs)
            currComb.pop()
            currSum -= arr[i]

def distinctCombinations(candidates:list, target:int):
    combs = [] #To keep track of combinations sum to target
    currComb = []
    combinations(candidates, target, 0, currComb, 0, combs)
    return combs

if __name__ == "__main__":
    print(distinctCombinations([3, 2, 5, 9, 1], 10))
