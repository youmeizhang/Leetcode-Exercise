class Solution:
    def isPossible(self, nums):
        frequency = collections.Counter(nums)
        tails = collections.defaultdict(int)

        n = len(nums)
        for i in range(n):
            if frequency[nums[i]] <= 0:
                continue

            frequency[nums[i]] -= 1

            if tails[nums[i] - 1] > 0:
                tails[nums[i]] += 1
                tails[nums[i] - 1] -= 1

            elif frequency[nums[i] + 1] and frequency[nums[i] + 2]:
                    tails[nums[i] + 2] += 1
                    frequency[nums[i]+2] -= 1
                    frequency[nums[i]+1] -= 1

            else:
                return False
        return True
            
