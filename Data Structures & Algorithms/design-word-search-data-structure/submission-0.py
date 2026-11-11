class TreeNode:
    def __init__(self):
        self.children = {}
        self.isLast = False
class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.isLast = True

    def search(self, word: str) -> bool:
        def dfs(node:TreeNode,i:int) -> bool:
            if len(word) == i:
                return node.isLast
            
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            
            if c not in node.children:
                return False
            return dfs(node.children[c], i + 1)

        return dfs(self.root, 0)

