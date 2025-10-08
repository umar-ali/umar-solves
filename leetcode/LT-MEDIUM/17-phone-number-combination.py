

# Given an string of digits (2-9)..
# Return All possible letter combination from telephone buttons
# "23" -> ["ad", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def letterCombination(digits:str) -> list[str]:

    digits_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    
    def permute(d:str, combinations:list[str] = []):
        if len(combinations) == 0:
            return [l for l in digits_map[d]] 
        res = []
        for l in digits_map[d]:
            res += [l + c for c in combinations]
        return res
    
    if len(digits) == 0:
        return []

    if len(digits) == 1:
        return permute(digits)
    return permute(digits[0], letterCombination(digits[1:]))

if __name__ == "__main__":
    print(letterCombination(''))
    print(letterCombination('2'))
    print(letterCombination('23'))


