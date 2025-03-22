import pprint
def count_divisors(num:int, p:int)->int:
    cnt = 0
    while num % p == 0 and num !=0:
        num //=p
        cnt+=1
    return cnt
 
def least_round(n, mat: list[list[int]]) -> tuple[int, str]:
    dp2 = [[(float("inf"),"")] * n for _ in range(n)]
    dp5 = [[(float("inf"),"")] * n for _ in range(n)]
    iz, jz = -1,-1
    
    #start 
    dp2[0][0] = (count_divisors(mat[0][0], 2), "")
    dp5[0][0] = (count_divisors(mat[0][0], 5), "")
    
    #first row only from left
    for j in range(1,n):
        dp2[0][j] = ( dp2[0][j-1][0]+count_divisors(mat[0][j], 2),dp2[0][j-1][1]+"R")
        dp5[0][j] = ( dp5[0][j-1][0]+count_divisors(mat[0][j], 5),dp5[0][j-1][1]+"R")

    #first column only from top 
    for i in range(1,n):
        dp2[i][0] = (dp2[i-1][0][0]+count_divisors(mat[i][0], 2), dp2[i-1][0][1]+"D")
        dp5[i][0] = (dp5[i-1][0][0]+count_divisors(mat[i][0], 5), dp5[i-1][0][1]+"D")

    pprint.pprint(dp2)   
    print()
    pprint.pprint(dp5)   
    print()
    for i in range(1, n):
        for j in range(1, n):
            if not mat[i][j]:
                iz, jz = i, j
            two_fs = count_divisors(mat[i][j], 2)
            five_fs = count_divisors(mat[i][j], 5)
            if dp2[i-1][j][0] < dp2[i][j-1][0]:
                dp2[i][j] = dp2[i-1][j][0] + two_fs, dp2[i-1][j][1]+"D"
            else:
                dp2[i][j] = dp2[i][j-1][0] + two_fs, dp2[i][j-1][1]+"R"

            if dp5[i-1][j][0] < dp5[i][j-1][0]:
                dp5[i][j] = dp5[i-1][j][0] + five_fs, dp5[i-1][j][1]+"D"
            else:
                dp5[i][j] = dp5[i][j-1][0] +five_fs, dp5[i][j-1][1]+"R"
            print("dp2")
            pprint.pprint(dp2)   
            print("dp5")
            pprint.pprint(dp5)   
            print()


    result = None 
    result_2 = dp2[n-1][n-1]
    result_5 = dp5[n-1][n-1]
    if result_2[0] < result_5[0]:
        result =  result_2
    else:
        result = result_5
    if iz != -1 and result[0] > 0:
        least= 1
        way = ""
        way += "D"*iz
        way += "R"*jz
        way +=  "D"*(n-iz)
        way += "R"*(n-jz)
        result = (least, way)
    return result

if __name__ == "__main__":
    n = int(input())
    mat = [list(map(int, input().split(" "))) for _ in range(n)]
    least, path = least_round(n,mat)
    print(f"{least}\n{path}")
        
        
        