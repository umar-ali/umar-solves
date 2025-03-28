def Solve(D):
    if D <= 1600:
        return "Yes"
    return "No"
    
    
if __name__ == "__main__":
    print(Solve(int(input())))