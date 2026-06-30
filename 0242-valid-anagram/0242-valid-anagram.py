class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        seen=[]
        if len(s)==len(t):
            for i in s:
                seen.append(i)
            for j in t:
                if j in seen:
                    a=0
                    seen.remove(j)    
                else:
                    a=1
                    break
            if a==0:
                return True
            else:
                return False
        else:
            return False    
         