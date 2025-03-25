def solve(s: str):
    if (l := len(s)) <= 1:
        return s
    sub_str = s[0]
    longest_ss = sub_str
    for idx in range(1, l):
        
        if (nxt_ch := s[idx]) not in sub_str:
            sub_str += nxt_ch
            if len(longest_ss) <= len(sub_str):
                longest_ss = sub_str
        else:
            sub_str = sub_str[sub_str.find(nxt_ch)+1:] + nxt_ch 
        
    print(longest_ss)


if __name__ == "__main__":
    s = input()
    solve(s)
