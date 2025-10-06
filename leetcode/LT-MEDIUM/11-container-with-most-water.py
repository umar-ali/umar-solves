

def maxArea(height:list[int]) -> int:
    i = 0
    j = len(height) -1
    mx = 0
    while i < j:
        mx = max(mx, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i+=1
        else:
            j-=1

    return mx
       
        
    

if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(maxArea(a))
    print(maxArea(a[::-1]))
    print(maxArea([1, 1]))
