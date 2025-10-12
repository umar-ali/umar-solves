
"""
# Roman Values

I -> 1
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1000


# sub form
IV -> 4
IX -> 9
XL -> 40
XC -> 9
CD -> 400
CM -> 900

examples ->

1234 MCCXXXIV
3749 MMMDCCXLIX
"""



def intToRoman(num:int) -> str:
    roman_value_map = {
        1   : 'I',
        5   : 'V',
        10  : 'X',
        50  : 'L',
        100 : 'C',
        500 : 'D',
        1000: 'M',
    }

    fives = ['V', 'L', 'D']
    tens = ['I','X', 'C', 'M']

    def mapNum2Roman(n:int, order:int):
        if n <= 3:
            return tens[order] * n
        elif n == 4:
            return  tens[order] + fives[order]
        elif n == 5:
            return fives[order]
        elif n <= 8:
            return fives[order] +  tens[order] * (n-5)
        elif n == 9:
            return  tens[order] + tens[order+1]


    res = ''
    i = 0
    while num > 0:
        n = num % 10
        print(num, n, i)
        res = mapNum2Roman(n, i) + res
        num //= 10
        i+=1
    return res



if __name__ == "__main__":
    print(intToRoman(3000))
    print(intToRoman(0))
