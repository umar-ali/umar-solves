
def Solution(likes, dislikes):
    setlikes = set(likes)
    setdislikes = set(dislikes)
    sol = setlikes - setdislikes
    ans = [len(sol)] + list(sol)
    return ans
    
likes = list()
dislikes = list()
with open("C:/python/py39/Google Hash Code/sampleinput.txt",'r+') as f:
    No_of_customers = int(f.readline())
    for i in range(1,No_of_customers):
        l = f.readline().split()
        if int(l[0]) > 0:
            likes += l[1:]
        d = f.readline().split()
        if int(d[0]) > 0:
            dislikes += d[1:]
    f.close()
    print("fileread")

sol = Solution(likes, dislikes)
with open("C:/python/py39/Google Hash Code/samplefiles.txt",'w+') as f:
    f.write(str(len(sol))+ " ")
    for i in range(1,len(sol)):
        f.write(str(sol[i])+" ")
    f.close()
    print("file written")


