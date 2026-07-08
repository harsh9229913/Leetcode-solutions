class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        a=True
        while l<=r:
            if s[l].isalnum()==False:
                l=l+1  
            elif s[r].isalnum()==False:
                r=r-1  
            elif s[l].lower()==s[r].lower():
                l=l+1
                r=r-1
                a=True  
            else:
                a=False
                break    
        return a 
        

