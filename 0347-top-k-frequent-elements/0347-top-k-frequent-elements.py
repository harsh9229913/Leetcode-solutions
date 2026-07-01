class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        lst=[]
        count=1
        f=0
        for i in nums:
            if not dct:
                dct[i]=count
            elif i in dct:
                dct[i]=dct[i]+1
            else:
                dct[i]=count    
     
        for i in range(k):
            a=max(dct,key=dct.get)
            lst.append(a)
            del dct[a]
        return lst  