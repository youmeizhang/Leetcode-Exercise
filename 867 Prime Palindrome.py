#time limit
#Solution 1
class Solution(object):
    def isPrime(self, num):
        if num < 2:
            return False
        else:
            n = int(math.sqrt(num)) + 1
            for i in range(2, n):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

    def isNumberPalindrome(self, n):
        return str(n) == str(n)[::-1]    

    def primePalindrome(self, N):
        while(not self.isPrime(N) or not self.isNumberPalindrome(N)):
            N += 1
            if N > 10**1 and N < 10**2 and N != 11:
                N = 10**2
            elif N > 10**3 and N < 10**4:
                N = 10**4
            elif N > 10**5 and N < 10**6:
                N = 10**6
            elif N > 10**7 and N < 10**8:
                N = 10**8
        return N
    
#Solution 2
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
