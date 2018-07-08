#time limit
class Solution(object):
    def isNumberPalindrome(self, n):
        return str(n) == str(n)[::-1]

    def isPrime(self, num):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False

    def primePalindrome(self, N):
        if N == 1:
            return 2
        
        res_new = list(filter(self.isPrime, filter(self.isNumberPalindrome, range(N-1,N**3))))
        #res_new = [x for x in res if self.isPrime(x)]
        
        n = len(res_new)
        left, right = 0, n
        while(left < right):
            mid = int((left + right) // 2)
            if res_new[mid] == N:
                return res_new[mid]
            elif res_new[mid] < N and N <= res_new[mid+1]:
                return res_new[mid+1]
            elif res_new[mid] > N:
                right = mid
            else:
                left = mid
        return res_new[mid]
