

#bi-153
#3499
def solve(s:str)->int:
    curr, prev, inactive, active, i = [0] * 5
    aug_str = "1" + s + "1"
    l = len(aug_str)
    
    while i < l and aug_str[i]=="1":
        active+=1
        i+=1

    while i < l and aug_str[i]=="0":
        prev+=1
        i+=1

    while i < l:
        while i < l and aug_str[i]=="1":
            active+=1
            i+=1
        if i == l:
            break
        while i < l and aug_str[i]=="0":
            curr+=1
            i+=1
        inactive = max(inactive, prev + curr )
        prev = curr
        curr = 0
    return active + inactive - 2


if __name__ == "__main__":
    s = input()
    print(solve(s))