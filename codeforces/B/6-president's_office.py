def solve(n, m, p, offc_mat):
    deputies= set()
    for i in range(n):
        for j in range(m):
            if offc_mat[i][j] == p:
                if j > 0 and offc_mat[i][j-1] != "."  and offc_mat[i][j-1] != p:
                    deputies.add(offc_mat[i][j-1])
                if j < m and (offc_mat[i][j+1] != "."  and offc_mat[i][j+1] != p):
                    deputies.add(offc_mat[i][j+1])
                if i > 0 and (offc_mat[i-1][j] != "." and offc_mat[i-1][j] != p):
                    deputies.add(offc_mat[i-1][j])
                if i < n and (offc_mat[i+1][j] != "." and offc_mat[i+1][j] != p):
                    deputies.add(offc_mat[i+1][j])
    print(deputies)
                
               
    pass
if __name__ =="__main__":
    n, m, p = tuple(input().split())
    offc_mat = [list(input().split()) for _ in range(int(n))]
    solve(int(n), int(m), p, offc_mat)