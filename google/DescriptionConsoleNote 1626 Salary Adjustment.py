class Solution:
    """
    @param a: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, a, target):
        # Write your code here.
        a = sorted(a)
        
        l = a[0]
        r = target // len(a) + 1
        
        while (l <= r):
            mid = (l + r) // 2
            total = 0
            for i in range(len(a)):
                if a[i] < mid:
                    total += mid
                else:
                    total += a[i]
            if total == target:
                return mid
            elif total > target:
                r = mid - 1
            else:
                l = mid + 1

        return mid
            
