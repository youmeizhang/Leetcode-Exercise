class Solution:
    def predictPartyVictory(self, senate):
        i = 0
        n = len(senate)
        dic = collections.Counter(senate)
        if dic["R"] == 0:
            return "Dire"
        if dic["D"] == 0:
            return "Radiant"

        senate = list(senate)
        count_r = 0
        count_d = 0

        while(True):
            if senate[i] == "R":
                if count_r < 1:

                    dic["D"] -= 1
                    count_d += 1
                    if dic["D"] == 0:

                        break
                else:
                    senate[i] = "0"
                    count_r -= 1

            elif senate[i] == "D":
                if count_d < 1:
                    dic["R"] -= 1
                    count_r += 1

                    if dic["R"] == 0:
                        break
                else:
                    senate[i] = "0"
                    count_d -= 1

            i += 1
            if i == n:
                i = 0

        return "Dire" if dic["R"] == 0 else "Radiant"
