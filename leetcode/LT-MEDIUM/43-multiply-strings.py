



def multiply(num1:str, num2:str) -> str:
    n, m = len(num1), len(num2)

    result = [0] * (n + m)

    for i in range(n -1, -1 , -1):
        for j in range(m -1, -1 , -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            sum_ = mul + result[i + j + 1]
            result[i + j + 1] = sum_ % 10 
            result[i + j] += sum_ // 10

    prod = ''.join(map(str, result)).lstrip('0')
    return prod if prod else "0"




if __name__ == "__main__":
    print(multiply("9"*200, "9"*200))
    print(multiply("9"*20, "9"*20))
