class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        for i in range(1, n-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                l = i - 1
                r = i + 1
                tmp = 3

                while (l > 0 and A[l] > A[l-1]):
                    tmp += 1
                    l -= 1
                
                while r < n - 1 and A[r] > A[r+1]:
                    tmp += 1
                    r += 1

                res = max(res, tmp)
        return res

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        l = [0] * (n)
        r = [0] * (n)
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                l[i] = l[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                r[i] = r[i+1] + 1

        res = 0
        for i in range(n):
            if l[i] and r[i]:
                res = max(res, l[i] + r[i] + 1)
        if res >= 3:
            return res
        else:
            return 0
        
        
