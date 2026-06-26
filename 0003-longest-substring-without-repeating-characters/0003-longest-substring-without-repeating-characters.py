class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=0
        dct={}
        dupl=[]
        if s=="":return 0
        else:
            i=0
            while i < len(s):
                if s[i] in dct.values():
                    i=next(key for key, value in dct.items() if value == s[i]) +1
                    dct.clear()
                    dupl.append(dup)
                    dup=1
                    dct[i]=s[i]
                elif s[i] not in dct.values():
                    dct[i]=s[i]
                    dup=dup+1
                    dupl.append(dup)
                i=i+1 
            return max(dupl)            