
def solve(s: str) -> bool:
    stack = []
    brackets = {
        "[":"]",
        "{":"}",
        "(":")",
    }
    for c in s:
        if c in brackets:
            stack.append(c)
        elif len(stack) > 0 and brackets[stack[-1]] == c:
            stack.pop()
        else:
            return False
    return len(stack) == 0
            
if __name__ == "__main__":
    test_cases = {
        "()": True,
        "()[]{}": True,
        "(]": False,
        "({})": True,
        "(((((":False,
        "}":False,
        "([)]":False, #Open brackets must be closed in the correct order.
    }
    for i, tc in enumerate(test_cases, 1):
        sol = solve(tc)
        assert (
            sol == test_cases[tc]
        ), f"Test Case :{i}, Failed: with input {tc} Expected {test_cases[tc]} Actual {solve(tc)}"
        print(tc, sol)

