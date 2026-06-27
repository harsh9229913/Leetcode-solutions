class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=0
        dct={}
        dupl=[]
        if s=="":return 0
        else:
            i=0
            while i < len(s):
                if s[i] in dct:
                    i=dct[s[i]]+1
                    dct.clear()
                    dct[s[i]]=i
                    dup=1
                    dupl.append(dup)
                elif s[i] not in dct:
                    dct[s[i]]=i
                    dup=dup+1
                    dupl.append(dup)
                i=i+1 
            return max(dupl)            