class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        res = []
        right = bisect.bisect_right(arr, x)
        left = right - 1

        while(left >= 0 and right < n):
            if len(res) == k:
                break
            if abs(arr[right] - x) >= abs(arr[left] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1

        while(left >= 0):
            if len(res) == k:
                break
            res.append(arr[left])
            left -= 1

        while(right < n):
            if len(res) == k:
                break
            res.append(arr[right])
            right += 1

        return sorted(res)
