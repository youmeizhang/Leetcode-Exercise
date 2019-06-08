# credit to: https://leetcode.com/problems/adding-two-negabinary-numbers/discuss/304444/Concise-or-Easy-to-understand-or-2-step-Python-solution

class Solution(object):
    def addNegabinary(self, arr1, arr2):
        a = arr1[::-1]
        b = arr2[::-1]
        l1 = len(a)
        l2 = len(b)
        total = 0

        for i in range(max(l1, l2)):
            curr = [a[i] if i < l1 else None, b[i] if i < l2 else None]
            if curr[0] != None:
                tmp = curr[0] * ((-2)**i)
                total += tmp
            if curr[1] != None:
                total += curr[1] * ((-2)**i)

        ans = []
        while total:
            ans.append(total % 2)
            total = -(total // 2)
        return ans[::-1] if ans else [0]
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
