# Definition for a binary tree node.
import collections


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for alp in word:
            node = node.children[alp]

        node.word = True

    def search(self, word: str) -> bool:
        node = self.root

        for alp in word:
            if alp not in node.children:
                return False
            else:
                node = node.children[alp]

        return node.word


    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for alp in prefix:
            if alp not in node.children:
                return False
            else:
                node = node.children[alp]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)