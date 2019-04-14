# credit to: http://zxi.mytechroad.com/blog/searching/127-word-ladder/
#Bi-BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}

        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set()
            for w in s1:
                new_words = [w[:i] + t + w[i+1:] for t in string.ascii_lowercase for i in range(l)]
                for new_word in new_words:
                    if new_word in s2:
                        return step + 1
                    if new_word not in wordDict:
                        continue
                    wordDict.remove(new_word)
                    s.add(new_word)
            s1 = s
        return 0

# BFS: time limited
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        dic = collections.Counter(wordList)
        
        if dic[endWord] == 0:
            return 0

        q = []
        q.append(beginWord)
        step = 0
        l = len(beginWord)
        while q:
            step += 1

            for size in range(len(q) - 1, -1, -1):
                w = q.pop(0)
                w_list = list(w)
                for i in range(l):
                    ch = w_list[i]
                    for j in range(ord('a'), ord('z')):
                        w_list[i] = chr(j)
                        w_str = ''.join(w_list)
                        if w_str == endWord:
                            return step + 1

                        if dic[w_str] == 0:
                            continue
                        if dic[w_str] > 0:
                            dic[w_str] == 0
                            if w_str not in q and w_str != w:
                                q.append(w_str)
                    w_list[i] = ch
        return 0
