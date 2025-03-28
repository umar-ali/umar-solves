def Solve(A,B):
    limak = 1
    Bob = 2
    while True:
    
        if limak > A:
            return "Bob"
        if Bob > B:
            return "Limak"
            
        A -= limak
        B -= Bob
        limak +=2
        Bob +=2
        
    
    
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        A,B = tuple(map(int, input().split()))
        print(Solve(A, B))