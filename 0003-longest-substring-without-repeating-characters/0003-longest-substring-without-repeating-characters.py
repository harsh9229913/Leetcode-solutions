class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=0
        dct={}
        left=0
        if s=="":return 0
        else:
            i=0
            for right in range(len(s)):
                if s[right] in dct and left<=right:
                   left = max(left, dct[s[right]] + 1)
                dct[s[right]]=right
                dup=max(dup,(right-left)+1)
        return dup   