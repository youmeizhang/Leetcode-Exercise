class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n == 0:
            return []
        dic = {}
        res = [0]
        for ele in nums[:k]:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        res[0] = max(dic)
        
        for i in range(1, n-k+1):
            old_ele = nums[i-1]
            if i + k - 1 < n:
                new_ele = nums[i+k-1]
                dic[old_ele] -= 1
                if dic[old_ele] == 0:
                    del dic[old_ele]
                if new_ele in dic:
                    dic[new_ele] += 1
                else:
                    dic[new_ele] = 1
                res.append(max(dic))
            else:
                res.append(max(dic))
        return res


# credit to: https://leetcode.com/problems/sliding-window-maximum/discuss/111560/Python-O(n)-solution-using-deque-with-comments

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res = []
        
        n = len(nums)
        for i in range(n):
            if q and i - q[0] == k:
                q.popleft()
            
            while q:
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
            
