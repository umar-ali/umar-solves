def Solution(Test_Case,CountryName):
    Vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if CountryName[-1] not in 'yY':
        if CountryName[-1] in Vowels:
            ruler  = "Alice"
        else:
            ruler = "Bob"
    else:
        ruler = "nobody"

    print(f"Case #{Test_Case}: {CountryName} is ruled by {ruler}.")
    
    

T = int(input())
for i in range(T):
    CountryName = input()
    Solution(i+1,CountryName)