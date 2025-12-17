def removeLeadingZeros(s:str) -> str:
    pos_1 = s.find('1')
    if pos_1 == -1:
        return '0'
    return s[pos_1:]

def addBinary(a:str, b:str) -> str:
    """Add give binary string"""

    #remove leading zero
    a, b = removeLeadingZeros(a), removeLeadingZeros(b)

    #swap by len
    if len(a) < len(b):
        a, b = b, a

    #equalize len
    b = '0' * (len(a) - len(b)) + b

    #loop over size in reverse and compute next bit with carry
    carry = 0
    out = ""
    for i in range(len(a)-1,-1,-1):
        bit_a, bit_b = int(a[i]), int(b[i])
        if carry and bit_a and bit_b:
            carry = 1
            out = '1' + out
        elif carry and bit_a or carry and bit_b or bit_a and bit_b:
            carry = 1
            out = '0' + out
        elif carry or bit_a or bit_b:
            carry = 0
            out = '1' + out
        else:
            carry = 0
            out = '0' + out
    if carry:
        out = str(carry) + out
    return out

if __name__ == "__main__":
    print(addBinary("11", "1")) #100
    print(addBinary("00", "1")) #1
    print(addBinary("00", "001")) #1
    print(addBinary("00", "000")) #0
    print(addBinary("0000", "111")) #1
    print(addBinary("1010", "111")) #1







                    




