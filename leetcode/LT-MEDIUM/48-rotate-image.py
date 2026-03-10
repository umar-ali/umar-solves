

def rotate(matrix: list[list[int]]) -> None:
    #intuition
    #swap matrix[i][j] with matrix[j][i] and vice versa
    #reverse all the row

    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        for j in range(i+1, c):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(r):
        matrix[i].reverse()

if __name__ == "__main__":
    import pprint
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    pprint.pp(matrix)
    rotate(matrix)
    print(matrix)
