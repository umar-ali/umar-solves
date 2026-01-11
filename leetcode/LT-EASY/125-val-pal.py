


def isPalindrome(s:str) -> bool:
   cleaned_s = "".join( c for c in s.lower() if c.isalnum())
   print(cleaned_s, cleaned_s[::-1])
   return cleaned_s == cleaned_s[::-1]

if __name__ == "__main__":
   print(isPalindrome("1r ec"))
   print(isPalindrome("a1a"))
   print(isPalindrome("A man, a plan, a canal: Panama"))