def solve(s: str):
    last_word = s.strip().split(" ")[-1]
    print(len(last_word))

if __name__ == "__main__":
    s = input()
    solve(s)

