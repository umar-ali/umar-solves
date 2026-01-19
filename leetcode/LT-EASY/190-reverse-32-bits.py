
def reverseBits(n:int) -> int:
    result = 0
    for i in range(32):
        #left shift res by 1.. to create room for one bit
        result <<= 1 # r = r << 1
        #take least significant bit of n and put in tha created bit of resutl
        result |= (n & 1)

        #discard least significant bit of n by rotating right
        n >>= 1
    return result


if __name__ == "__main__":
    print(reverseBits(43261596))

