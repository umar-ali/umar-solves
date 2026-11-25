
def solve(s:str, t:str) -> None:
    alpha = {c:i+1 for i, c in enumerate("abcdefgh")}

    s1, s2 = alpha[s[0]], int(s[1])
    t1, t2 = alpha[t[0]], int(t[1])

    h = ""
    if s1 > t1:
        h = 'L'
    elif s1 < t1:
        h = 'R'
    h_dis = abs(t1 - s1)

    v = ""
    if s2 > t2:
        v = 'D'
    elif s2 < t2:
        v = 'U'
    v_dis = abs(t2 - s2)

    moves = max(h_dis, v_dis)

    print(moves)
    #king's  moves
    for _ in range(moves):
        move = ""
        if h_dis > 0:
            move += h
            h_dis -= 1

        if v_dis > 0:
            move += v
            v_dis -= 1

        print(move)




if __name__ == "__main__":
    s = input()
    t = input()
    solve(s, t)

