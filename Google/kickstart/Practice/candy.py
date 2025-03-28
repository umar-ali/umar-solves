def Solution(Test_case, bags, kids, array):
    Total_Candies = 0
    for i in range(bags):
        Total_Candies += array[i]
    Remaining_Candies = Total_Candies % kids

    print(f"Case #{Test_case}: {Remaining_Candies}")

T = int(input())
for i in range(T):
    (bags, kids) = tuple(map(int,input().split()))
    array = list(map(int, input().split()))
    Solution(i+1, bags, kids, array)
