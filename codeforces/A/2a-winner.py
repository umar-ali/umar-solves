

def find_the_winner(rounds: list[int]) -> str:

    #calculate final score
    scores = {}
    for name, score in rounds:
        scores[name] = scores.get(name, 0) + int(score)
    final_score = max(scores.values())
    scores.clear()

    #find first person to score final_score
    for name, score in rounds:
        scores[name] = scores.get(name, 0) + int(score)
        print(name, final_score, scores[name])
        if final_score <= scores[name]:
            return name
        
if __name__ == "__main__":
    n = int(input())
    rounds = []
    while n > 0:
        rounds.append(tuple(input().split(' ')))
        n-=1
    print(find_the_winner(rounds))
