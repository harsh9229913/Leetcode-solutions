import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        lst=[]
        count=1
        numheap=[]
        for i in nums:
            if not dct:
                dct[i]=count
            elif i in dct:
                dct[i]=dct[i]+1
            else:
                dct[i]=count    
     
        for x,y in dct.items():
            heapq.heappush(numheap,(y,x))
            if len(numheap) > k:
                heapq.heappop(numheap)
        return [x for y, x in numheap]
