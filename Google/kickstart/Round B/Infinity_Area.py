import math

def Area_of_circle(R):
    pie = math.pi
    return pie*(R**2)

def Solution(R, A, B):
    Total_Area = 0
    right = True
    while(R>=1):
        if(right):
            Total_Area += Area_of_circle(R)
            R *= A
            right = False
        else:
            Total_Area += Area_of_circle(R)
            R = math.floor(R/B)
            right = True
    return Total_Area






if __name__ == "__main__":
    t = int(input())
    for i in range(1,t+1):
        R, A, B = tuple(map(int, input().split()))
        print(f"Case #{i}: {str.format('{0:.6f}',Solution(R, A, B))}")
