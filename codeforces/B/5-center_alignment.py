def solve(lines:list[str]) -> None:
    long_len = 0
    for line in lines:
        if long_len < len(line):
            long_len = len(line)
    print("*"*(long_len+2))
    l_pad = 0
    r_pad = 0
    for line in lines:
        diff = long_len - len(line)
        pad = diff%2
        if pad !=0:
            if not r_pad:
                r_pad = pad
                l_pad = 0
            elif not l_pad:
                l_pad = pad
                r_pad = 0
            left_spaces = "-"*(diff//2+l_pad)
            right_spaces = "-"*(diff//2+r_pad)
            print(f"*{left_spaces}{line}{right_spaces}*")
            continue
        left_spaces = "-"*(diff//2)
        right_spaces = "-"*(diff//2)
        print(f"*{left_spaces}{line}{right_spaces}*")
    print("*"*(long_len+2))
    return 
    


if __name__ == "__main__":
    lines = []
    while line:=input():
        if not line:
            break
        lines.append(line)
    solve(lines)