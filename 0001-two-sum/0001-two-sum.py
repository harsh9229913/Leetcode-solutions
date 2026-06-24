class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
           s=nums[i]
           for j in range(len(nums)):
             if j==i:
                break
             else:
                p=nums[j]
             if s+p==target:
                return[i,j]   

