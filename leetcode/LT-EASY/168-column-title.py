ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_SIZE = 26

def convertToTitle(columnNumber:int) -> str:
    if columnNumber <= ALPHA_SIZE:
        return ALPHA[columnNumber - 1]

    div, mod = divmod(columnNumber, ALPHA_SIZE)
    if mod == 0:
        div-=1
    return convertToTitle(div) + convertToTitle(mod)

if __name__ == "__main__":
    print(convertToTitle(701))
    print(convertToTitle(26))
    print(convertToTitle(28))
    print(convertToTitle(52))
    print(convertToTitle(78))
