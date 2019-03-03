class Solution(object):
    def palindromePairs(self, words):
        res = set()

        def palindrome(string):
            l = 0
            r = len(string) - 1
            while l <= r:
                if string[l] == string[r]:
                    l += 1
                    r -= 1

                else:
                    return False
            return True

        dic = collections.defaultdict(int)

        for i in range(len(words)):
            dic[words[i]] = i

        for i in range(len(words)):
            if words[i] and palindrome(words[i]):
                if "" in dic:
                    res.add((dic[""], i))
                    res.add((i, dic[""]))


            rword = words[i][::-1]
            if words[i] and rword in dic:
                if i != dic[rword]:
                    res.add((i, dic[rword]))
                    res.add((dic[rword], i))

            for x in range(1, len(words[i])):
                left, right = words[i][:x], words[i][x:]
                rleft, rright = left[::-1], right[::-1]
                if palindrome(left) and rright in dic:
                    res.add((dic[rright], i))
                if palindrome(right) and rleft in dic:
                    res.add((i, dic[rleft]))

        return list(res)
