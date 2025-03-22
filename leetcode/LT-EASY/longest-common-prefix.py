


def longestCommonPrefix(strs:list[str]):
    sorted_strs = sorted(strs, key=lambda s: len(s))
    start = sorted_strs[0]
    if len(strs) == 1:
        return start
    for i in range(len(start)):
        if isAll:= not all(s.startswith(start[:i+1]) for s in sorted_strs[1:]):
            return start[:i]
    return start
    
if __name__ == "__main__":
    strs = ["flower","flow", "flight"], ["dog", "race","zoo"], ["ab", "a"]
    for s in strs:
        print(longestCommonPrefix(s))