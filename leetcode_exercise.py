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