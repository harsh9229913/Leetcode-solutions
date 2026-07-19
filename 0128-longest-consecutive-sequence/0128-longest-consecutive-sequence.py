class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        a=0
        c=1
        vis=set()
        lst=[]
        if not nums:return 0
        for i in s:
            a=0
            c=1
            if i-1 not in s:
                start=i   
                d=start+1 
            else:continue    
            while a==0:
                if d in s:
                    c=c+1
                    lst.append(c)
                    d=d+1
                else:
                    lst.append(c)
                    a=1
        return max(lst)            


