#MEXanized Arry

def solve(n, k, x):
   if n < k or k-1 > x: return -1
   #sm = sum(range(0, k)); n-=k
   sm = (k*(k-1))/2; n-=k
   if k == x: sm += n *(x-1)
   else: sm += n * x
   return sm 
if __name__ == "__main__":
   t = int(input())
   for i in range(1,t+1):
        a = input()
        n, k, x = tuple([int(i) for i in a.split()])
        print(solve(n, k, x))