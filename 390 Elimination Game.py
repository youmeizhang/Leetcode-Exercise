class Solution(object):
    def lastRemaining(self, n):
        head = 1
        step = 1
        remain = n
        status = True
        while remain > 1:
            if status or remain % 2 == 1:
                head += step
            step *= 2
            remain /= 2
            status = not status
        return head
    
#time limited
#1
class Solution(object):
    def lastRemaining(self, n):
        a = list(range(1, n+1))
        cnt = 0
        while (len(a) > 1):
            if cnt % 2 == 0:
                a = [a[i] for i, v in enumerate(a) if i % 2 == 1]
                cnt += 1
                a = list(reversed(a))
            else:
                a = [a[i] for i, v in enumerate(a) if i % 2 == 1]
                a = list(reversed(a))
                cnt += 1
        return a[0]
    
#2
class Solution(object):
    def lastRemaining(self, n):
        nums = [i for i in range(1, n+1)]
        left_to_right = True
        while(len(nums) > 1):
            if left_to_right:
                nums = nums[1::2]
                left_to_right = False
            else:
                nums = nums[-2::-2][::-1]
                left_to_right = True
        return nums[0]
    
#3
def lastRemaining(self, n):
    a = list(range(1, n+1))
    cnt = 0
    while (len(a) > 1):
        if cnt % 2 == 0:
            a = [a[i] for i, v in enumerate(a) if i % 2 == 1]
            cnt += 1
        else:
            if len(a) % 2 == 1:
                a = [a[i] for i, v in enumerate(a) if i % 2 == 1]
            else:
                a = [a[i] for i, v in enumerate(a) if i % 2 == 0]
            cnt += 1
    return a[0]
