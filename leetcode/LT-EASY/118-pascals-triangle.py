
def generate(numRows:int) -> list[list[int]]:

    pascal_triangle = []

    for i in range(numRows):
        row = []
        coef = 1
        for j in range(0, i+1):
            row.append(coef)
            #using identity -> Next binomial coefficient from the previous one:
            # C(n, k+1) = C(n, k) * (n - k) // (k + 1)
            coef = coef * (i - j ) // (j + 1)
        pascal_triangle.append(row)
    return pascal_triangle


print(generate(5))


