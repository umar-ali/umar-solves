
def generate(rowIndex:int) -> list[list[int]]:
    row = []
    for i in range(rowIndex+1):
        coef = 1
        for j in range(0, i+1):
            if i == rowIndex:
                row.append(coef)

            #using identity -> Next binomial coefficient from the previous one:
            # C(n, k+1) = C(n, k) * (n - k) // (k + 1)
            coef = coef * (i - j ) // (j + 1)
        
    return row


print(generate(3))
print(generate(2))
print(generate(5))


