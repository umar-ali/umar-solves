def Solve(R):
    if 1 <= R <=50:
        return 100
    elif 51 <= R <= 100:
        return 50
    else:
        return 0

if __name__ == "__main__":
    R = int(input())
    print(Solve(R))
    