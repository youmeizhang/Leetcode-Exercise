class Solution:
    def minWindow(self, s, t):
        n = len(s)
        left = 0
        right = 0
        dic_t = collections.Counter(t)
        dic_s = collections.defaultdict(int)
        cnt = 0
        minLen = float('inf')
        res = ""
        while right < n:
            dic_s[s[right]] += 1

            if s[right] in dic_t and dic_s[s[right]] <= dic_t[s[right]]:
                cnt += 1

            while(left <= right and cnt == len(t)):      
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left : right + 1]
                dic_s[s[left]] -= 1
                if s[left] in dic_t and dic_s[s[left]] < dic_t[s[left]]:
                    cnt -= 1
                left += 1

            right += 1
        return res
        
