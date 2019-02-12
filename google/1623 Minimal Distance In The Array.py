class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """
    def minimalDistance(self, a, b):
        # Write your code here 
        a.sort()
        res = []
        
        def binary(a, ele):
            l = 0
            r = len(a) - 1
            while (l <= r):
                mid = (l + r) // 2
                if a[mid] == ele:
                    return a[mid]
                
                elif mid == 0:
                    return a[mid] if abs(ele - a[mid]) <= abs(ele - a[mid + 1]) else a[mid + 1]
    
                elif mid == len(a) - 1:
                    return a[mid] if abs(ele - a[mid]) <= abs(ele - a[mid - 1]) else a[mid - 1]
                
                elif a[mid - 1] < ele and a[mid + 1] > ele:
                    tmp = min(abs(ele - a[mid - 1]), abs(ele - a[mid]), abs(ele - a[mid + 1]))
                    if abs(ele - a[mid - 1]) == tmp:
                        return a[mid - 1]
                    elif abs(ele - a[mid]) == tmp:
                        return a[mid]
                    else:
                        return a[mid + 1]
                elif a[mid] > ele:
                    r = mid - 1
                else:
                    l = mid + 1
            return a[mid]
        
        for ele in b:
            res.append(binary(a, ele))
        return res
