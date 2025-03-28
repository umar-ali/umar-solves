#PRACLIST
def Solve(Total, attempted):
    return Total-attempted
 
if __name__ == "__main__":
    total, attempted = tuple(map(int, input().split()))
    print(Solve(total, attempted))

    