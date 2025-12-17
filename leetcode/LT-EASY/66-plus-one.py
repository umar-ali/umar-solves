

def plusOne(digits:list[int]) -> list[int]:
    if digits[-1] < 9:
        return digits[:-1] + [digits[-1] + 1]
    out = [0]
    overf = 1
    for i in digits[:-1][::-1]:
        if i == 9 and overf:
            out = [0] + out
            overf = 1
        else:
            out = [i+overf] + out
            overf = 0
    if overf:
        return [overf] + out
    return out




if __name__ == "__main__":
    print(plusOne([1, 2, 3])) # [1, 2, 4]
    print(plusOne([9])) # [1,0]
    print(plusOne([1, 2, 9])) # [1, 3, 0]
    print(plusOne([1])) # [1, 3, 0]
    print(plusOne([9,1])) # [9,2]
    print(plusOne([9,9])) # [1,0,0]

