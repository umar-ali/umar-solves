"""
    three_timers = {"M", "C", "X", "I"}
    one_timers = {
        "D",
        "L",
        "V",
    }  # this one timers can preced three timers to make 4, 9, , 40, 90, , 400, 900
"""
def solve(roman: str) -> int:
    """convert roman number to integer"""
    symbol_mapper = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    high = None
    num = 0
    ctr = 0
    ln = len(roman)
    if ln == 1:
        return symbol_mapper[roman]
    for i in range(ln):
        s = roman[i]
        if not high:
            high = s
            ctr += 1
            print("case 1", s, high, ctr, num)
            continue
        if s == high:
            ctr += 1
            print("case 2",s, high, ctr, num)
            continue
        elif high and (s != high or i + 1 == ln):
            if symbol_mapper[high] < symbol_mapper[s]:
                num += symbol_mapper[s] - symbol_mapper[high]
                if ctr:
                    ctr -= 1
                num += ctr * symbol_mapper[high]
                high = None
                ctr = 0
                print("case 3",s, high, ctr, num)
                continue
            num += ctr * symbol_mapper[high]
            high = s
            ctr = 1
            print("case 4",s, high, ctr, num)
    if high and ctr > 0:
        num += ctr * symbol_mapper[high]
        print("case 5",s, high, ctr, num)
    return num


if __name__ == "__main__":
    print(solve("XXVII"))
