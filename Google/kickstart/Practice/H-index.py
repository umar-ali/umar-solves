
def countcite(pos,citation):
    count = 0
    for i in citations:
        if citations[pos] >= i:
            count +=1
    return count


def Solution(Test_Case,papers, citations):
    output  = [1]
    for i in range(1, papers):
        if countcite(i,citations[:i+1]) >= citations[i]:
            output.append(citations[i])
        else:
            output.append(output[-1])

    print(output)

       
        


    #print(f"Case #{Test_Case}: {output}")


T = int(input())
for i in range(T):
    papers = int(input())
    citations = list(map(int,input().split()))
    Solution(i+1, papers, citations)