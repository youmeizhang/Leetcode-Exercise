class Solution(object):
    def prevPermOpt1(self, A):
        n = len(A)
        for i in range(n-2, -1, -1):
            tmp1 = A[i+1:]
            tmp = sorted(tmp1)
            l = 0
            r = len(tmp) - 1
            target = A[i]
            while l <= r:
                mid = (l + r) // 2
                if mid < len(tmp) - 1 and tmp[mid+1] >= target and tmp[mid] < target:
                    break 
                elif mid == 1 and tmp[mid] >= target and tmp[mid-1] < target:
                    mid = mid - 1
                    break
                elif tmp[mid] == target:
                    r = mid - 1
                elif tmp[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            max_ = tmp[mid]

            for j in range(len(tmp1)):
                if tmp1[j] == max_:
                    idx = j
                    break
            if max_ < A[i]:
                A[i], A[idx+i+1] = max_, A[i]
                return A
        return A
