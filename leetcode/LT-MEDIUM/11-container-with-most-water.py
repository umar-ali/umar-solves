

def maxArea(height:list[int]) -> int:
    m = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            m = max(m, min(height[i], height[j]) * (j - i))

    return m




if __name__ == "__main__":
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))
