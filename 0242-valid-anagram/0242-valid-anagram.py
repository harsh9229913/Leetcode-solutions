class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        seen={}
        freq=1
        if len(s)==len(t):
            for i in s:
                if i in seen:
                    seen[i]=seen[i]+1

                else:
                    seen[i]=freq
            for j in t:
                if j in seen:
                    seen[j]=seen[j]-1
                    if seen[j]<0:
                       a=1
                       break
                    else:
                       a=0 
                else:
                    a=1
                    break
            if a==0:
                return True
            else:
                return False    
        else:
            return False      
