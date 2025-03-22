

def solve(path:str):
    c, r = 0, 0
    field = []
    for m in path:
        if m == "L":
            c-=1
        elif m == "R":
            c+=1
        elif m == "U":
            r-=1
        elif m == "D":
            r+=1
        
    


if __name__ == "__main__":
    path = input()
    solve(path)