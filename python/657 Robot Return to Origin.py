class Solution:
    def judgeCircle(self, moves):
        dic = collections.Counter(moves)
        if dic["U"] == dic["D"] and dic["R"] == dic["L"]:
            return True
        return False
