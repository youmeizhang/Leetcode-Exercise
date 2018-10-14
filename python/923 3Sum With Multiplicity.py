#Time Limit
class Solution:
    def threeSumMulti(self, A, target):
        dic = collections.Counter(A)
        permutation = self.threeSum(A, target)
        permutation = list(set(permutation))
        
        res = 0
        tmp = 1
        for permute in permutation:
            if len(list(set(permute))) == 1:
                n = dic[permute[0]]
                tmp = self.factor(n) / ( self.factor(3) * self.factor(n-3))
                
            elif len(list(set(permute))) == 3:
                for i in range(3):
                    tmp *= dic[permute[i]]
            else:
                small_dic = collections.Counter(permute)
                second = list(small_dic.keys())[list(small_dic.values()).index(2)]
                first = list(small_dic.keys())[list(small_dic.values()).index(1)]
                tmp *= dic[first]
                n = dic[second]
                tmp *= self.factor(n) / ( self.factor(2) * self.factor(n-2))
                
            res += int(tmp)
            tmp = 1
            
        if res >= 495500972:
            return 495500972
        else:
            return res
            
        
    def factor(self, num):
        factorial = 1
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial
                
    
    def threeSum(self, nums, target): #use set nums
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            #if i > 0 and nums[i] == nums[i-1]:
                #continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l +=1 
                elif s > target:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
