class Solution:
    def isLongPressedName(self, name, typed):
        if name == typed:
            return True
        i = j = 0
        while (i < len(name) and j < len(typed)):
            if name[i] == typed[j]:
                j += 1
                i += 1
            elif name[i-1] == typed[j]:
                j += 1
            else:
                return False
        if i == len(name):
            return True
        else:
            return False
