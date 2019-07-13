class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = list(filter(lambda x: x.split(' ')[1].isdigit(), logs))
        letter = list(filter(lambda x: not x.split(' ')[1].isdigit(), logs))

        letter = sorted(letter, key = lambda x : [x.split(' ')[1:], x.split(' ')[0]])
        return letter + digit
