

def find_the_winner(rounds: list[int]) -> str:
    """
        this solution fails for input as follows:
        >4
        >andrew 10
        >mike 12
        >mike -2
        >andrew 0
    """
    winner, mx = tuple(rounds[0].split(' '))
    mx = int(mx)
    scores = {winner: int(mx)}
    for r in rounds[1:]:
        name, score = tuple(r.split(' '))
        score = int(score)
        scores[name] = scores.get(name, 0) + score
        if scores[name] > mx:
            mx = scores[name]
            winner = name
    
    return winner


if __name__ == "__main__":
    n = int(input())
    rounds = []
    while n > 0:
        rounds.append(input())
        n-=1
    print(find_the_winner(rounds))
