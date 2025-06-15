def isPalindrome(s):
    left=0
    right=len(s)-1
    while left<=right:
        if s[left]==s[right]:
            left=left+1
            right=right-1
        else:
            return False
    return True


print(isPalindrome("ssgss"))
print(isPalindrome("wedeq"))


bank=set()
def isPaliPalindrome(s):
    print(bank)
    if s in bank:
        return True
    if len(s)==1:
        return True
    if isPalindrome(s):
        mid=len(s)//2
        front=s[0:mid]
        back=s[mid+1:]
        if isPaliPalindrome(front):
            bank.add(front)
        if isPaliPalindrome(back):
            bank.add(back)
        return front in bank and back in bank
        
    else:
        return False

print(isPaliPalindrome("abacaba"))
print(isPaliPalindrome("abba"))
        
        
            
