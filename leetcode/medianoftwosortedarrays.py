"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        result = nums1 + nums2
        result.sort()

        # To find median

        if len(result) % 2 != 0:
            pos = len(result)//2
            return result[pos]
        else:
            pos = len(result)//2
            res = (result[pos] + result[pos-1])/2
            return res
