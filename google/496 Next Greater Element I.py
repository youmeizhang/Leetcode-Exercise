class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            if idx == len(nums2) - 1:
                res.append(-1)
            else:
                for j in range(idx, len(nums2)):
                    if nums2[j] > nums1[i]:
                        res.append(nums2[j])
                        break
                if j == len(nums2) - 1 and nums2[j] <= nums1[i]:
                    res.append(-1)
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
