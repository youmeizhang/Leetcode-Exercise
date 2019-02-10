#credit to: YichengLi

class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        def func(A, K):
            cnt = [0 for _ in range(len(A) + 1)]
            j = 0
            n = len(A)
            wd = 0
            res = 0
            for i in range(n):
                cnt[A[i]] += 1
                if cnt[A[i]] == 1:
                    wd += 1
                while wd > K:
                    cnt[A[j]] -= 1
                    if cnt[A[j]] == 0:
                        wd -= 1
                    j += 1
                res += i - j + 1
            return res

        return func(A, K) - func(A, K - 1)
