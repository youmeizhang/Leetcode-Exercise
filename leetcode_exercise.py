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
