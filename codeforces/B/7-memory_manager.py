ILL = "ILLEGAL"

def solve(m, commands):
    id = 0
    for cmd in commands:
        if cmd is "defragment":
            pass
        elif "alloc" in cmd:
            pass
        elif "erase" in cmd:
            pass


if __name__ =="__main__":
    t,m = tuple(map(int, input().split()))
    commands = [input() for _ in range(t)]
    solve(m, commands)
        