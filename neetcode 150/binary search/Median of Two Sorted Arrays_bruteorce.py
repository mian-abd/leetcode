class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = 0.00000
        temp = []
        for a in nums1:
            temp.append(a)
        for a in nums2:
            temp.append(a)
        temp = sorted(temp)
        m = len(temp)//2
        if len(temp) % 2 == 0:
            res = (temp[m] + temp[m-1]) / 2 #remmber that it starts from 0
        else:
            res = temp[m]

        return res
