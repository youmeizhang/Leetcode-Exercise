#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:04:53 2018

@author: yumi.zhang
"""
#Update Everyday

#April 25th, 2018
#Contains Duplicate
def containsDuplicate(self, nums):
    tempset = set()
    if len(nums) == 0:
        return False
    for i in nums:
        if i in tempset:
            return True
        tempset.add(i)
    return False

#Intersection of two Arrays
def intersection(self, nums1, nums2):
    tempset = []
    for i in nums1:
        for j in nums2:
            if i==j and j not in tempset:
                tempset.append(i)
    return tempset

#Happy Number
def squaresum(self, n):
    sum = 0
    while(n>0):
        temp = n % 10
        sum += temp * temp
        n = n//10
    return sum

def isHappy(self, n):
    fast = slow = n
    while True:
        slow = self.squaresum(slow)
        fast = self.squaresum(fast)
        fast = self.squaresum(fast)
        if slow == fast:
            break
    return slow==1

#isomorphic strings
def isIsomorphic(self, s, t):
    hashmap = {}
    for i in range(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]] = t[i]
        elif hashmap[s[i]] != t[i]:
            return False
    
    #mapval = [hashmap[k] for k in hashmap]
    #return len(mapval) == len(set(mapval))
    test = []
    for k in hashmap:
        test.append(hashmap[k])
    return len(test) == len(set(test))

#Minimum Index Sum of Two Lists
class Solution(object):
    def findRestaurant(self, list1, list2):
        hashmap = {}
        for i in range(0, len(list1)):
            if list1[i] not in hashmap:
                if list1[i] in list2:
                    hashmap[list1[i]] = i+list2.index(list1[i])
        value = min(hashmap.values())
        result = []
        for keys, values in hashmap.items():
            if values == value:
                result.append(keys)
        
        return result
    
#First Unique Character in a String
def findUniqueChar(self, s):
    if len(s)==0:
        return -1
    s_dict = {}
    s = list(s)
    for x in s:
        s_dict[x] = s.count(x)
    result = []
    for keys, values in s_dict.items():
        if values == 1:
            result.append(keys)
    if len(result) == 0:
        return -1
    else: 
        index = {}
        for i in result:
            index[i] = s.index(i)
        min_value = min(index.values())
        return(min_value)
        
#Contains Duplicate II (time limit)
def containsNearbyDuplicate(self, nums, k):
    if len(nums) < 2:
        return False
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False

#Contains Duplicate II (solution 2 without time limit)
def containsNearbyDuplicate(nums, k):
    if len(nums) < 2:
        return False
    temp = {}
    for i in range(0, len(nums)):
        if nums[i] in temp and abs(i-temp[nums[i]]) <=k:
            return True
        else:
            temp[nums[i]] = i
    return False

#April 28th, 2018
#Binary Tree, implement preorder, inorder and postorder recursively
class Tree(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    
    def preorder(root):
        if root is None:
            return
        else:
            print(root.data)
            preorder(root.left)
            preorder(root.right)
        
    def inorder(root):
        if root is None:
            return
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)
            
    def postorder(root):
        if root is None:
            return
        else:
            postorder(root.left)
            postorder(root.right)
            print(root.data)

#build a simple tree for test
root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

#implement it iteratively
def preorder(root):
    result = []
    if root is None:
        return result
    stack = []
    node = root
    while node or stack:
        while node:
            result.append(node.data)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return result

def inorder(root):
    result = []
    if root is None:
        return result
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.data)
        node = node.right
    return result

def levelorder(root):
    result = []
    if root is None:
        return result
    current_level = [root]
    while current_level:
        next_level = []
        level_result = []
        for temp in current_level:
            if temp.left != None:
                next_level.append(temp.left)
            if temp.right != None:
                next_level.append(temp.right)
            level_result.append(temp.data)
        result.append(level_result)
        current_level = next_level
    return result

#another solutions: using queue, but the format doesnot meet the requirement of leetcode
def levelorder(root):
    result = []
    if root is None:
        return result
    myqueue = []
    node = root
    myqueue.append(node)
    while myqueue:
        node = myqueue.pop(0)
        if node.left != None:
            myqueue.append(node.left)
        if node.right != None:
            myqueue.append(node.right)
        result.append(node.data)
    return result

#April 29th, 2018 
#Maximum Depth of Binary Tree
def maxDepth(self, root):
    if root == None:
        return 0
    else:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#Symmetric Tree
class Solution(object):
    def leftandright(self, p, q):
        if p == None and q == None:
            return True
        if p != None and q != None and p.val == q.val:
            return self.leftandright(p.left, q.right) and self.leftandright(q.left, p.right)  #be careful of this
        return False
    
    def isSymmetric(self, root):
        if root:
            return self.leftandright(root.left, root.right)
        return True

#path sum
def hasPathSum(self, root, sum):
    if root == None:
        return False
    if root.left == None and root.right == None:
        return root.val == sum
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

#Construct Binary Tree from Inorder and Postorder Traversal
def buildTree(self, inorder, postorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(postorder[len(postorder) - 1])
    idx = inorder.index(postorder[len(postorder)-1])
    root.left = self.buildTree(inorder[0: idx], postorder[0: idx])
    root.right = self.buildTree(inorder[idx+1: len(inorder)], postorder[idx: len(postorder) - 1])
    return root

#Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(self, preorder, inorder):
    if len(inorder) == 0:
        return None
    if len(inorder) == 1:
        return TreeNode(inorder[0])
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1: idx], inorder[0: idx])
    root.right = self.buildTree(preorder[idx+1: len(preorder)], inorder[idx+1: len(inorder)])
    return root

#Populating Next Right Pointers in Each Node
def connect(self, root):
    if root and root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        else:
            root.next = None
        self.connect(root.left)
        self.connect(root.right)
        
#Populating Next Right Pointers in Each Node II
def connect(self, root):
    if root:
        if root.left and root.right:
            root.left.next = root.right
            temp = root.next
            while temp:
                if temp.left:
                    root.right.next = temp.left
                    break
                if temp.right:
                    root.right.next = temp.right
                    break
                temp = temp.next
        elif root.left:
            temp = root.next
            while temp:
                if temp.left:
                    root.left.next = temp.left
                    break
                if temp.right:
                    root.left.next = temp.right
                    break
                temp = temp.next
        elif root.right:
            temp = root.next
            while temp:
                if temp.left:
                    root.right.next = temp.left
                    break
                if temp.right:
                    root.right.next = temp.right
                    break
                temp = temp.next
        self.connect(root.right)
        self.connect(root.left)  
        
#Lowest Common Ancestor of a Binary Tree
def lowestCommonAncestor(self, root, p, q):
    if not root:
        return root
    if root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left != None and right != None:
        return root
    if left != None:
        return left
    else:
        return right
#Serialize and Deserialize Binary Tree
class Codec:
    def serialize(self, root):
        result = []
        def preorder(root):
            if not root:
                result.append('null')
            else:
                result.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ''.join(result)

    def deserialize(self, data):
        if len(data) == 0:
            return None
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                else:
                    root = TreeNode(int(val))
                    root.left = build()
                    root.right = build()
                return root
        return build()
    
#Binary Search
def search(self, nums, target):
    for i in range(0, len(nums)):
        if nums[i]==target:
            return i
    else:
        return -1
    
#Sqrt(x)
def mySqrt(self, x):
    if x == 0:
        return 0
    left = 1
    right = x / 2 + 1
    while(left <= right):
        mid = (left + right) / 2
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

#Guess Number Higher or Lower
def guessNumber(self, n):
        if n == 0:
            return 0
        left = 1
        right = n
        while (left <= right): 
            mid = (left + right) / 2 #mid = (left + (right - left) >> 1)
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1
                
#Search in Rotated Sorted Array
def search(self, nums, target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[left]: #left is ascending
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        
        if nums[mid] < nums[right]: #right is ascending
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

#First Bad Version
def firstBadVersion(self, n):
    if n == 0:
        return 0
    left = 1
    right = n
    while left <= right:
        mid = (left + right) / 2
        if isBadVersion(mid):
            if mid == 1 or not isBadVersion(mid-1):
                return mid
            right = mid - 1
        else:
            left = mid + 1
#Find Peak Element
def findPeakElement(self, nums):
    if len(nums) == 1:
        return 0
    left = 0
    right = len(nums) - 1
    while left<right:
        mid = (left + right) / 2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return left

#Find Minimum in Rotated Sorted Array
def findMin(self, nums):
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) / 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]

#Search for a Range
def searchRange(self, nums, target):
    if len(nums)==0:
        return [-1, -1]
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            result = [0, 0]
            if nums[left] == target: result[0] = left
            if nums[right] == target: result[1] = right
            for i in range(mid, right+1):
                if nums[i] != target: result[1] = i-1; break
            for i in range(mid, left-1, -1):
                if nums[i] != target: result[0] = i+1; break
            return result
    return [-1, -1]

#Find K Closest Elements
def findClosestElements(self, arr, k, x):
    if len(arr) == 0 or len(arr) < k:
        return None
    left = 0
    right = len(arr) - 1
    while (right - left + 1) > k:
        if abs(x - arr[right]) < abs(x- arr[left]):
            left += 1
        else:
            right -=1
    return arr[left: right+1]

#def myPow(self, x, n):
    if n==0:
        return 1
    elif n < 0:
        return 1 / self.myPow(x, -n)
    elif n % 2:
        return self.myPow(x*x, n/2)*x
    else:
        return self.myPow(x*x, n/2)
    
#Valid Perfect Square
def isPerfectSquare(self, num):
    if num == 0 or num == 1:
        return True
    left = 0
    right = num
    while left <= right:
        mid = (left + right) / 2
        if mid*mid == num:
            return True
        elif mid*mid > num:
            right = mid-1
        else:
            left = mid + 1       
    return False

#Find Smallest Letter Greater Than Target (环形有序)
def nextGreatestLetter(self, letters, target):
    letters_new = set(map(ord, letters))
    for i in range(1, 27):
        candidate = ord(target) + i
        if candidate > ord('z'):
            candidate -= 26
        if candidate in letters_new:
            return chr(candidate)
        
#Find Minimum in Rotated Sorted Array II
def findMin(self, nums):
    if len(nums) == 0:
        return 0
    left = 0
    right = len(nums) - 1
    while (left < right):
        mid = (left + right) / 2
        mid = int(mid)
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1
    return nums[left]

#Two Sum II - Input array is sorted
def twoSum(self, numbers, target):
    left = 0
    right = len(numbers) - 1
    while (left<right):
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
            
#Two Sum II - Input array is sorted (Solution two: but time limit)
def twoSum(self, numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j] == target-numbers[i]:
                return [i+1, j+1]
            
#Find the Duplicate Number
def findDuplicate(self, nums):
    left = 1
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        count = sum(x <= mid for x in nums)
        if count > mid:
            right = mid - 1
        else:
            left = mid + 1
    return left

#Find the Duplicate Number (Solution two: but time limit)
def findDuplicate(self, nums):
    result = []
    for i in range(0, len(nums)):
        if nums[i] not in result:
            result.append(nums[i])
        else:
            return nums[i]

#Median of Two Sorted Arrays
class Solution(object):

    def getKth(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k/2, lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B):
        totallen = len(A) + len(B)
        if totallen % 2 == 1: 
            return self.getKth(A, B, totallen/2 + 1)
        else:
            return (self.getKth(A, B, totallen/2) + self.getKth(A, B, totallen/2 + 1)) * 0.5
        
#Binary Search Tree Iterator
class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.pushleft(root)
        """
        :type root: TreeNode
        """
    def hasNext(self):
        return self.stack
        """
        :rtype: bool
        """    
    def next(self):
        top = self.stack.pop()
        self.pushleft(top.right)
        return top.val
        """
        :rtype: int
        """
    def pushleft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

#Search in a Binary Search Tree
class Solution(object):
    def searchBST(self, root, val):
        if root is None:
            return None
        else:
            node = root
            if node.val == val:
                return node
            else:
                return self.searchBST(node.left, val) or self.searchBST(node.right, val)
            
#Kth Smallest Element in a BST
def kthSmallest(self, root, k):
    if root is None:
        return None
    else:
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while x <= k and stack:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left  
    return node.val

#Number of Islands
class Solution(object):
    def numIslands(self, grid):
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        visit = [[False for i in range(n)] for j in range(m)]
        
        def check(x, y):
            if x < m and y < n and x>=0 and y>=0 and grid[x][y] == '1' and visit[x][y] == False:
                return True
        
        def dfs(x, y):
            nrow = [1, 0, -1, 0]
            ncol = [0, 1, 0, -1]
            for k in range(4):
                newx = x + nrow[k]
                newy = y + ncol[k]
                if check(newx, newy):
                    visit[newx][newy] = True
                    dfs(newx, newy)
        
        count = 0
        for row in range(m):
            for col in range(n):
                if check(row, col):
                    visit[row][col] = True
                    dfs(row, col)
                    count += 1
        return count
    
#Sort Colors
class Solution(object):
    def sortColors(self, nums):
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in nums:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            else:
                count_2 += 1
        for i in range(0, count_0):
            nums[i] = 0
        for i in range(count_0, count_0+count_1):
            nums[i] = 1
        for i in range(count_1+count_0, len(nums)):
            nums[i] = 2
            
#Top K Frequent Elements
def topKFrequent(self, nums, k):
    temp ={}
    for i in range(0, len(nums)):
        if nums[i] not in temp:
            temp[nums[i]] = 1
        else:
            temp[nums[i]] += 1
    s = sorted(temp.items(), key=operator.itemgetter(1), reverse=True)#sort a dict
    result = []
    for i in range(k):
        result.append(s[i][0])
    return result

#Kth Largest Element in an Array
def findKthLargest(self, nums, k):
    if len(nums) == 0:
        return None
    else:
        new_nums = sorted(nums, reverse=True)
        return new_nums[k-1]
    
#Merge Intervals
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x:x.start)
        length = len(intervals)
        res = []
        for i in range(length):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res
    
#Search a 2D Matrix II
class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        y = len(matrix[0])-1
        def binarySearch(nums, left, right):
            while left <= right:
                mid = (left+right) / 2
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid + 1
            return right
        
        for x in range(len(matrix)):
            y = binarySearch(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
            
#Jump Game
class Solution(object):
    def canJump(self, nums):
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True        
        return False
    
#Unique Paths
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for i in range(n)] for i in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]
        return dp[m-1][n-1]

#Factorial Trailing Zeroes (time limit)
class Solution(object):
    def trailingZeroes(self, n):
        if n==0:
            return 0
        result = n
        while (n-1) > 0:
            result = result*(n-1)
            n -= 1
        result = str(result)    
        zerovalue = 0
        for i in range(len(result)-1, -1, -1):
            if result[i] != '0':
                zerovalue = len(result) - i - 1
                break
        return zerovalue
    
#Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        res = 0
        while n > 0:
            n = n/5
            res += n
        return res
    
#Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, s):
        sum = 0
        for i in s:
            sum = sum*26 + ord(i) - 64
        return sum
    
#Divide Two Integers
def divide(dividend, divisor):
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        if abs(dividend) < abs(divisor):
            return 0
    sum = 0
    res = 0
    count = 0
    a = abs(dividend)
    b = abs(divisor)
    while a >= b:
        sum = b
        count = 1
        while sum + sum <= a:
            sum += sum
            count += count
        a -= sum
        res += count
        res 
            
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        res = -res
    return res

#Divide Two Integers
class Solution(object):
    def divide(self, dividend, divisor):
        max_int = 2147483647
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            k = 0
            temp = divisor
            while dividend >= temp:
                dividend -= temp
                quotient += 1 << k
                temp <<= 1
                k += 1
        quotient = sign * quotient
        if quotient > max_int:
            return max_int
        return quotient
    
#Fraction to Recurring Decimal
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        negflag = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        loopDict = {}
        loopStr = None
        cnt = 0
        numList = []
        while True:
            numList.append(str(numerator / denominator))
            cnt += 1
            numerator = (numerator % denominator) * 10
            if numerator == 0:
                break
            loc = loopDict.get(numerator)
            if loc:
                loopStr = "".join(numList[loc:cnt])
                break
            loopDict[numerator] = cnt
        ans = numList[0]
        if len(numList) > 1:
            ans += "."
        if loopStr:
            ans += "".join(numList[1: len(numList) - len(loopStr)]) + "(" + loopStr + ")"
        else:
            ans += "".join(numList[1:])
        if negflag:
            ans = "-" + ans
        return ans
#Insert Delete GetRandom O(1)    
import random
class RandomizedSet(object):

    def __init__(self):
        self.datamap = {}
        self.datalist = []      

    def insert(self, val):
        if val in self.datamap:
            return False
        else:
            self.datamap[val] = len(self.datalist)
            self.datalist.append(val)
            return True

    def remove(self, val):
        if val not in self.datamap:
            return False
        else:
            idx = self.datamap[val]
            tail = self.datalist.pop()
            if idx < len(self.datalist):
                self.datalist[idx] = tail
                self.datamap[tail] = idx
            del self.datamap[val]
            return True
        

    def getRandom(self):
        return random.choice(self.datalist)
    
#Sum of Two Integers
class Solution(object):
    def getSum(self, a, b):
        while b != 0:
            carry = a & b
            a = (a^b) % 0x100000000
            b = (carry<<1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000 + 1)
    
#Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '/' and tokens[i] != '*':
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                elif tokens[i] == '-':
                    stack.append(b-a)
                elif tokens[i] == '*':
                    stack.append(a*b)
                elif tokens[i] == '/' and a*b < 0:
                    stack.append(-(-b/a))
                else:
                    stack.append(b/a)
        return stack.pop()
    
#Majority Element
class Solution(object):
    def majorityElement(self, nums):
        result = {}
        for i in range(0, len(nums)):
            if nums[i] not in result:
                result[nums[i]] = 1
            else:
                result[nums[i]] += 1
        inverse = [(value, key) for key, value in result.items()]
        if max(inverse)[0] > len(nums) / 2:
            value = max(inverse)[1]
        return value
    
#Task Scheduler
class Solution(object):
    def leastInterval(self, tasks, n):
        output = [0] * 26
        for i in tasks:
            output[ord(i) - ord('A')] = output[ord(i) - ord('A')] + 1
            
        count = 0
        len_0 = 0
        max_0 = max(output)
        for i in output:
            if i == max_0:
                count += 1
        return max(len(tasks), (max_0-1)*(n+1) + count)
#Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        dict = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        def dfs(num, string, res):
            if length == 0:
                return res
            if num == length:
                res.append(string)
                return
            for i in dict[digits[num]]:
                dfs(num + 1, string + i, res)
                
        res = []            
        length = len(digits)
        dfs(0, '', res)
        return res
    
#Longest Increasing Subsequence
class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        temp = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i] and temp[j] + 1 > temp[i]:
                    temp[i] = temp[j] + 1
        return max(temp)
    
#Generate Parentheses    
class Solution(object):
    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)
    
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res
    
#Permutations
class Solution(object):
    def permute(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            res = []
            for i in range(0, len(nums)):
                x = nums[i]
                xs = nums[:i] + nums[i+1:]
                for p in self.permute(xs):
                    res.append([x]+p)
            return res
        
#Subsets
class Solution(object):
    def subsets(self, nums):
        self.res = []
        def dfs(nums, temp, i):
            self.res.append(temp[:])
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i+1)
                temp.pop()
        dfs(nums, [], 0)
        return self.res
    
#Word Search
class Solution(object):
    def exist(self, board, word):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    
    def dfs(self, board, row, col, word):
        if len(word) == 0:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
            return False
        temp = board[row][col]
        board[row][col] = ''
        result = self.dfs(board, row+1, col, word[1:]) or self.dfs(board, row-1, col, word[1:]) or self.dfs(board, row, col+1, word[1:]) or self.dfs(board, row, col-1, word[1:])
        board[row][col] =temp
        return result
    
#Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        listA = [1]
        listB = [1]
        tempA = 1
        for i in range(0, len(nums)-1):
            tempA = tempA*nums[i]
            listA.append(tempA)
        tempB = 1
        tempNums = list(reversed(nums))
        for j in range(0, len(tempNums)-1):
            tempB = tempB * tempNums[j]
            listB.append(tempB)
        listBre = list(reversed(listB))
        result = []
        for a in range(0, len(listA)):
            result.append(listA[a]*listBre[a])
        return result
    
#Spiral Matrix
class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        k = 0
        l = 0
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        direction = 0
        res = []
        while True:
            if direction == 0:
                for i in range(l, n+1):
                    res.append(matrix[k][i])
                k += 1
            if direction == 1:
                for i in range(k, m+1):
                    res.append(matrix[i][n])
                n -= 1
            if direction == 2:
                for i in range(n, l-1, -1):
                    res.append(matrix[m][i])
                m -= 1
            if direction == 3:
                for i in range(m, k-1, -1):
                    res.append(matrix[i][l])
                l += 1
            if l > n or k > m:
                return res
            direction = (direction + 1) % 4
            
#4Sum II
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        res = 0
        cnt = collections.defaultdict(int)
        for a in A:
            for b in B:
                cnt[a+b] += 1
        for c in C:
            for d in D:
                res += cnt[-(c+d)]
        return res
    
#Container With Most Water
class Solution(object):
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
    
#First Missing Positive
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(0, n):
            if i+1 != nums[i]:
                return i+1
        return n+1
    
#Longest Consecutive Sequence
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums_new =sorted(nums)
        count = 1
        res = []
        for i in range(0, len(nums_new)-1):
            if nums_new[i+1] - nums_new[i] == 1:
                count += 1
            elif nums_new[i+1] - nums_new[i] == 0:
                count += 0
            else:
                res.append(count)
                count = 1
        res.append(count)
        return max(res)
    
#Basic Calculator II
class Solution(object):
    def calculate(self, s):
        tokens = iter(re.findall('\d+|\S', s))
        res = 0
        sign = 1
        for token in tokens:
            if token.isdigit():
                num = int(token)
            elif token in '+-':
                res += sign * num
                sign = 1 if token == '+' else -1
            else:
                temp = int(next(tokens))
                num = num * temp if token == '*' else num // temp
        return res + sign * num
    
#Sliding Window Maximum
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 0 or k > len(nums):
            return []
        res = []
        for i in range(0, len(nums)-k+1):
            xs = nums[i : i + k]
            res.append(max(xs))
        return res
    
#Wiggle Sort II
class Solution(object):
    def wiggleSort(self, nums):
        new_nums = sorted(nums)
        size = len(nums)
        for x in range(1, size, 2) + range(0, size, 2):
            nums[x] = new_nums.pop()

#Max Points on a Line
class Solution:
    def maxPoints(self, points):
        if len(points) <= 1:
            return len(points)
        maxpoint = 1
        for i in range(0, len(points)-1):
            vertical = 1
            slopes = {}
            samepoints = 0
            curmax = 1
            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samepoints += 1
                    continue
                elif points[i].x == points[j].x:
                    vertical += 1
                else:
                    slop = (points[i].y - points[j].y) * 1.0/ (points[i].x - points[j].x)
                    slopes.setdefault(slop, 1)
                    slopes[slop] += 1
                    if slopes[slop] > curmax:
                        curmax = slopes[slop]
            maxpoint = max(max(curmax, vertical)+samepoints, maxpoint)
        return maxpoint

#Kth Smallest Element in a Sorted Matrix
class Solution:
    def kthSmallest(self, matrix, k):
        low = matrix[0][0]
        high = matrix[-1][-1]
        loc = 0
        while low <= high:
            mid = (low + high) >>1
            loc = sum(bisect.bisect_right(m, mid) for m in matrix)
            if loc >= k:
                high = mid -1
            else:
                low = mid + 1
        return low

#Find Pivot Index
class Solution:
    def pivotIndex(self, nums):
        add_sum = sum(nums)
        left_sum = 0
        for i in range(0, len(nums)):
            add_sum -= nums[i]
            if add_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
        return -1
    
#Merge k Sorted Lists
class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if not lists or n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = int(n / 2)
            return self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])
            
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
