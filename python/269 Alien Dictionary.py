# credit to: https://www.cnblogs.com/lightwindy/p/8531872.html

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_degree = {}
        out_degree = {}
        nodes = set()
        res = []
        zero_in_degree_queue = collections.deque()
        
        for word in words:
            for c in word:
                nodes.add(c)
        
        
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
                return ""
            
            self.findEdges(words[i-1], words[i], in_degree, out_degree)
            
        
        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)
        
        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            res.append(precedence)
            
            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)
                        
                del out_degree[precedence]
        
        if out_degree:
            return ""
        
        return "".join(res)
        
    def findEdges(self, word1, word2, in_degree, out_degree):
        n = min(len(word1), len(word2))
        for i in range(n):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = set()
                    
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = set()
                
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break
                
        
        
