class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        row = len(words)
        for i in range(row):
            column_str = ""
            for j in range(row):
                column_str += words[j][i]
            if words[i] == column_str:
                continue
            else:
                return False
        return True
