

def divide(dividend:int, divisor: int) -> int:
    #infer sign
    if dividend == 0:
        return 0
    
    #Handle Overflow
    #if both dividend and divisor are int, so their qoutient must be int i.e,. [-2**31 <= q 2**31 -1]
    #except if dividend is -2**31, and divisor -1 which result in 2**31, which is out of bound
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    
    isNegative = (dividend < 0) ^ (divisor < 0)

    #abosolute value
    dividend = abs(dividend)
    divisor = abs(divisor)

    #subtract divsisor from dividend
    #until it becomes lesser than divisor
    #keep qoutient incrementing
    qoutient = 0
    
    #bit manipulation
    #total number of bits. as it is int 32 bit (positions 31...0)
    for i in range(31, -1, -1):
        u = divisor << i  
        if dividend >= u:
            dividend -= u
            qoutient |= (1 << i) # set the ith bit of quotient
   
    if isNegative:
        qoutient = (~qoutient) + 1

    return qoutient


if __name__ == "__main__":
    print(divide(10, 3)) # 3
    print(divide(10, -3)) # -3
    print(divide(-10, -3)) # 3