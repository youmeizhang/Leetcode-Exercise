class Solution(object):
    def validMountainArray(self, A):
        if A == [] or len(A) < 3:
            return False
        n = len(A)
        l, r = 0, n - 1
        while(l <= r):
            mid = (l + r) // 2
            if mid == n-1 or mid == 0:
                return False 
            elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                left = 1
                while(left < mid):
                    if A[left] <= A[left - 1]:
                        return False
                    else:
                        left += 1
                right = mid + 1
                while(right < n-1):
                    if A[right+1] >= A[right]:
                        return False
                    else:
                        right += 1
                return True
            elif A[mid] > A[mid - 1]: #increasing, on the left, mountain is on the right
                l = mid + 1
            else:
                r = mid - 1
        return False
