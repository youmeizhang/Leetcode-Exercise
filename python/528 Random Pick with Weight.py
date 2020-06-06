# tutorial: https://www.youtube.com/watch?v=v-_aEMtgnkI

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w_acc = []
        n = len(w)
        total = 0
        for i in range(n):
            total += w[i]
            self.w_acc.append(total)
       

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(1, self.w_acc[-1])  
        return self.binary_search(x)
        
        
    def binary_search(self, target):
        l = 0
        r = len(self.w_acc) - 1
        while l < r:
            mid = l + (r - l) / 2
            if self.w_acc[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
