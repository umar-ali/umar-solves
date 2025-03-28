#HS08TEST
def Solve(amt, bal):
    if amt >= bal or amt%5 !=0:
        return bal
    else:
        bal -= amt
        bal -= .5
    return bal
        
if __name__ == "__main__":
    withdrawAMT, accBal = tuple(map(float, input().split()))
    print("{:.2f}".format(Solve(withdrawAMT, accBal)))
        
    