#[2,7,11,19]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
           s=nums[i]
           a=target-s
           if a in dict:
            return[i,dict[a]]
           else:
            dict[s]=i

