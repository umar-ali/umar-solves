
def Solve(N, old_password):
    SpecialChars = ['#','@','*','&']
    Alphabhets = "abcdefghijklmnopqrstuvwxyz"
    uppalpha = Alphabhets.upper()
    digits = "1234567890"
    upperAlpha = lowerAlpha = Specialcheck = digitcheck = False
    u = set(old_password)
    
    for i in digits:
        if i in u:
            digitcheck = True
            break
            
    for i in Alphabhets:
        if i in u:
            lowerAlpha = True
            break
        if i.upper() in u:
            upperAlpha = True
            break
            
    for i in SpecialChars:
        if i in u:
            Specialcheck = True
            break
    
    
            
    """for i in u:
        if i.isalnum():
            if i.isdigit():
                digitcheck = True
            else:
                if i in Alphabhets:
                    lowerAlpha = True
                else:
                    upperAlpha = True
        else:
            if i in SpecialChars:
                Specialcheck = True"""
    i = 0
    if digitcheck and upperAlpha and lowerAlpha and Specialcheck and N >= 7:
        return old_password
    if N < 7:
        while N < 7:
            if not digitcheck:
                old_password += digits[N%10]
                N+=1
            if not upperAlpha:
                old_password += Alphabhets[i%26].upper()
                N+=1
            if not lowerAlpha:
                old_password += Alphabhets[i%26]
                N+=1
            if not Specialcheck:
                old_password += SpecialChars[i%4]
                N+=1
            i+=1
            
    else:
        if not digitcheck:
            old_password += digits[3]
        if not upperAlpha:
            old_password += Alphabhets[1].upper()
        if not lowerAlpha:
            old_password += Alphabhets[1]
        if not Specialcheck:
            old_password += SpecialChars[1]
    return old_password

	
if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        N = int(input())
        old_password = input()
        print(f"Case #{i}: {Solve(N, old_password)}")