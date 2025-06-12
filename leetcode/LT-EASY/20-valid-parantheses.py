
def solve(s: str) -> bool:
    # left_curl, left_paran, left_sqr = 0, 0, 0
    brackets = {
        "{":0,
        "(":0,
        "[":0
    }
    pairs = {
        "}":"{",
        ")":"(",
        "]":"["
    }
    for c in s:
        if c in brackets:
            brackets[c] += 1 
        elif brackets[pairs[c]] >= 1:
            brackets[pairs[c]] -= 1
        else:
            return False
    return all([ v == 0 for v in brackets.values()])




#TODO submit to lt
if __name__ == "__main__":
    test_cases = {
        "()": True,
        "()[]{}": True,
        "(]": False,
        "({})": True,
        "(((((":False,
        "}":False,
    }
    for i, tc in enumerate(test_cases, 1):
        sol = solve(tc)
        assert (
            sol == test_cases[tc]
        ), f"Test Case :{i}, Failed: with input {tc} Expected {test_cases[tc]} Actual {solve(tc)}"
        print(tc, sol)

