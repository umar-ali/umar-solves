def Solve():
   N = int(input())
   Fabrics = list()
   for i in range(N):
      T = input().split()
      T[1] = int(T[1])
      T[2] = int(T[2])
      Fabrics.append(tuple(T))
   SortedByada = sorted(Fabrics, key = lambda x: (x[0], x[2]))
   SortedBycharles = sorted(Fabrics, key = lambda x: (x[1], x[2]))
   cnt = 0
   
   #and SortedByDurability[i] == SortedByUID[i] and  SortedByColor[i]
   for i in range(len(Fabrics)):
      if SortedByada[i] == SortedBycharles[i]:
         cnt +=1
   return cnt
             
if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        result = Solve()
        print(f"Case #{i}: {result}")
