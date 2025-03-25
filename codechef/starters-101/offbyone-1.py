def add_off1(a, b):return int(str(a+b)+"1")

if __name__ == "__main__":
    a, b = tuple([int(x) for x in input().split()])
    print(add_off1(a, b))