



def multiply(num1:str, num2:str) -> str:
    return str(int(num1) * int(num2)) #direct conversion not allowed


if __name__ == "__main__":
    print(multiply("9"*200, "9"*200))
    print(multiply("9"*20, "9"*20))