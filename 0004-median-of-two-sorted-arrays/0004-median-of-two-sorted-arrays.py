class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fl=nums1+nums2
        fl.sort()
        if len(fl)%2==0:
            a=len(fl)
            b=int((a/2)-1)
            c=b+1
            m=(fl[b]+fl[c])/2
            return m
        else:
            a=len(fl)
            b=int(a//2)
            m=fl[b]
            return m


        