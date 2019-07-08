# credit to: http://bookshadow.com/weblog/2017/07/16/leetcode-design-search-autocomplete-system/

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.sentences = set()
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.buffer = ''
        self.stimes = collections.defaultdict(int)
        self.trie = TrieNode()
        for s, t in zip(sentences, times):
            self.stimes[s] = t
            self.addSentence(s)
        self.tnode = self.trie

    def addSentence(self, s):
        node = self.trie
        for letter in s:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
            child.sentences.add(s)
            
    def input(self, c: str) -> List[str]:
        ans = []
        if c != "#":
            self.buffer += c
            if self.tnode:
                self.tnode = self.tnode.children.get(c)
            if self.tnode:
                ans = sorted(self.tnode.sentences, key = lambda x: (-self.stimes[x], x))[:3]
        else:
            self.stimes[self.buffer] += 1
            self.addSentence(self.buffer)
            self.buffer = ''
            self.tnode = self.trie
        return ans


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
