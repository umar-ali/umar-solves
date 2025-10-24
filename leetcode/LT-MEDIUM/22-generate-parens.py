


def generateParenthesis(n:int) -> list[str]:
    ...

if __name__ == "__main__":
    print(generateParenthesis(1)) #["()"]
    print(generateParenthesis(2)) #["()()", "(())"]
    print(generateParenthesis(3)) #["((()))","(()())","(())()","()(())","()()()"]
    print(generateParenthesis(4))