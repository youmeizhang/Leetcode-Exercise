class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        
        res = []
        for i in range(n):
            start = nums2.index(nums1[i])
            for j in range(start, m):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
                elif j == m - 1 and nums2[j] <= nums1[i]:
                    res.append(-1)
        return res
