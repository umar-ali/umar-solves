

def maxArea(height:list[int]) -> int:
    m = 0
    last = -1
    for i in range(len(height)):
        if height[i] > last:
            for j in range(i+1, len(height)):
                m = max(m, min(height[i], height[j]) * (j - i))
            last = height[i]
    return m




if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print(maxArea(a))
    print(maxArea(a[::-1]))
    print(maxArea([1, 1]))
