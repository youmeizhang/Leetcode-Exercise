#Solution 1
class Solution(object):
    def longestSubstring(self, s, k):
        cnt = collections.Counter(s)
        filters = [x for x in cnt if cnt[x] < k]
        if not filters: return len(s)
        tokens = re.split('|'.join(filters), s)
        return max(self.longestSubstring(t, k) for t in tokens)
        
#Solution 2
class Solution(object):
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
