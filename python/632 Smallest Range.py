class Solution:
    def smallestRange(self, nums):
        dic = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                dic.append([nums[i][j], i])
        dic.sort(key = lambda x : x[0])
        value = []
        idx = []
        for tup in dic:
            value.append(tup[0])
            idx.append(tup[1])

        dic_t = collections.defaultdict(int)
        for i in range(len(nums)):
            dic_t[i] = 1

        dic_s = collections.defaultdict(int)

        left, right, cnt, minLen = 0, 0, 0, float('inf')
        res = [0, 0]

        while right < len(value):
            dic_s[idx[right]] += 1
            if idx[right] in dic_t and dic_s[idx[right]] <= dic_t[idx[right]]:
                cnt += 1
            while(left <= right and cnt == len(dic_t)):
                if minLen > value[right] - value[left]:
                    minLen = value[right] - value[left]
                    res = [value[left], value[right]]
                dic_s[idx[left]] -= 1
                if idx[left] in dic_t and dic_s[idx[left]] < dic_t[idx[left]]:
                    cnt -= 1
                left += 1
            right += 1
        return res  
    
