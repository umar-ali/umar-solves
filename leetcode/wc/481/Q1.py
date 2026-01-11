def mirrorDistance( n:int) -> int:
    return abs(n - int("".join(reversed(str(n)))))

print(mirrorDistance(5))
print(mirrorDistance(10))
print(mirrorDistance(25))