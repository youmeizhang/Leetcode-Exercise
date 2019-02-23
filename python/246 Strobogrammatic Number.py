class Solution(object):
    def isStrobogrammatic(self, word):
        left = 0
        right = len(word) - 1
        while left <= right:
            if word[left] == word[right] and (word[left] == "1" or word[left] == "8" or word[left] == "0"):
                left += 1
                right -= 1
            elif word[left] == "6" and word[right] == "9":
                left += 1
                right -= 1
            elif word[left] == "9" and word[right] == "6":
                left += 1
                right -= 1
            else:
                return False
        return True
