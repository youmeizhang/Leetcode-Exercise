class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        left = 0
        zero = 0

        for right in range(len(A)):
            if A[right] == 0:
                zero += 1

            while zero > K:

                if A[left] == 0:
                    zero -= 1

                left += 1

            res = max(res, right - left + 1)
        return res
        
