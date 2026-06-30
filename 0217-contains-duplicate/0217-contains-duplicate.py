class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rep=set()
        a=1
        for i in nums:
            if i in rep:
                a=0
                break
            else:
                rep.add(i)
                a=1

        if a==0:
            return True
        else:
            return False    
